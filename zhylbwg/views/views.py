# -*- coding: utf-8 -*-
'''===================================
@Project：wisdomShop
@Author：班婕妤
@Date：5/3/2020 下午1:50
@Company：深圳市智慧养老宝科技有限公司
@Motto：心有猛虎，细嗅蔷薇
@Python_Version：3.7.3
@Django_Version：2.1.5
======================================='''
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from zhylbwg.serializers import UserSerializer
from zhylbwg.models import loginModels
from rest_framework.permissions import AllowAny
from rest_framework.schemas import SchemaGenerator
from rest_framework.schemas.generators import LinkNode, insert_into
from rest_framework.renderers import *
from rest_framework_swagger import renderers
from rest_framework.response import Response


# Create your views here.

class MySchemaGenerator(SchemaGenerator):

    def get_links(self, request=None):
        # from rest_framework.schemas.generators import LinkNode,
        links = LinkNode()

        paths = []
        view_endpoints = []
        for path, method, callback in self.endpoints:
            view = self.create_view(callback, method, request)
            path = self.coerce_path(path, method, view)
            paths.append(path)
            view_endpoints.append((path, method, view))

        # Only generate the path prefix for paths that will be included
        if not paths:
            return None
        prefix = self.determine_path_prefix(paths)

        for path, method, view in view_endpoints:
            if not self.has_view_permissions(path, method, view):
                continue
            link = view.schema.get_link(path, method, base_url=self.url)
            # 添加下面这一行方便在views编写过程中自定义参数.
            link._fields += self.get_core_fields(view)

            subpath = path[len(prefix):]
            keys = self.get_keys(subpath, method, view)

            # from rest_framework.schemas.generators import LinkNode, insert_into
            insert_into(links, keys, link)

        return links

    # 从类中取出我们自定义的参数, 交给swagger 以生成接口文档.
    def get_core_fields(self, view):
        return getattr(view, 'coreapi_fields', ())


class SwaggerSchemaView(APIView):
    _ignore_model_permissions = True
    exclude_from_schema = True

    # from rest_framework.permissions import AllowAny
    permission_classes = [AllowAny]
    # from rest_framework_swagger import renderers
    # from rest_framework.renderers import *
    renderer_classes = [
        CoreJSONRenderer,
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = MySchemaGenerator(title='xxxxx',
                                      description='''xxxxx''')

        schema = generator.get_schema(request=request)

        # from rest_framework.response import Response
        return Response(schema)
