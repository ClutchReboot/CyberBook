from . import tools, utils


class ConjureTraversalList:
    def __init__(
            self,
            custom_payload: list = None,
            web_files: list = None,
            default_payload: bool = True,
            url_encoded: bool = True,
            null_bytes: bool = True,
            repeat: int = 5
    ):

        self.custom_payload = custom_payload
        self.default_payload = default_payload
        self.url_encoded = url_encoded
        self.null_bytes = null_bytes
        self.repeat = repeat + 1

        self.web_files = list()
        if web_files:
            self.web_files = self.web_files + web_files

        self.traversal_list = list()
        self.traversal_list_length = 0

    def _update(self, traversal_list: list):
        self.traversal_list = self.traversal_list + traversal_list
        self.traversal_list_length = len(self.traversal_list)

    def create(self) -> list:
        directives = [f"{directive * i}" for i in range(2, self.repeat) for directive in tools.directives]
        self._update(traversal_list=directives)

        if self.default_payload:
            default_payload_included = utils.add_payload(traversal_list=directives, payloads=tools.payloads)
            self._update(traversal_list=default_payload_included)

        if self.custom_payload:
            custom_payload_included = utils.add_payload(traversal_list=directives, payloads=self.custom_payload)
            self._update(traversal_list=custom_payload_included)

        if self.web_files:
            web_files_included = utils.add_web_file(traversal_list=self.traversal_list, web_files=self.web_files)
            self._update(traversal_list=web_files_included)

        if self.url_encoded:
            url_encoded_included = utils.full_url_encoder(unencoded=self.traversal_list)
            self._update(traversal_list=url_encoded_included)

        if self.null_bytes:
            null_bytes_included = utils.add_null_bytes(traversal_list=self.traversal_list, null_bytes=tools.null_bytes)
            self._update(traversal_list=null_bytes_included)

        return self.traversal_list
