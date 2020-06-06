import json

from rest_framework.test import APIClient as DRFClient


class APIClient(DRFClient):
    DEFAULT_FORMAT = "json"

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.user = user
            self.force_authenticate(user=user)

    def get(self, path, *args, **kwargs):
        return self._make_request(path, "get", *args, **kwargs)

    def patch(self, path, *args, **kwargs):
        return self._make_request(path, "patch", *args, **kwargs)

    def post(self, path, *args, **kwargs):
        return self._make_request(path, "post", *args, **kwargs)

    def put(self, path, *args, **kwargs):
        return self._make_request(path, "put", *args, **kwargs)

    def delete(self, path, *args, **kwargs):
        return self._make_request(path, "delete", *args, **kwargs)

    def _build_detail_url(self, path, obj):
        if obj is None:
            return path
        return path + str(obj.pk) + "/"

    def _make_request(self, path, method, *args, **kwargs):
        path = self._build_detail_url(path, kwargs.pop("obj", None))
        expect = kwargs.pop("status_code", None)
        as_response = kwargs.pop("as_response", False)

        kwargs["format"] = kwargs.get("format", self.DEFAULT_FORMAT)

        method = getattr(super(), method)

        response = method(path, *args, **kwargs)

        if expect:
            assert response.status_code == expect, response.data

        if as_response:
            return response

        return self._decode(response)

    def _decode(self, response):
        if getattr(response, "data", None):
            return response.data

        content = response.content.decode("utf-8", errors="ignore")
        if "application/json" in response._headers["content-type"][1]:
            return json.loads(content)
        else:
            return content
