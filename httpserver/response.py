class HttpResponse:
    def __init__(
        self,
        verson: str,
        status_code: int,
        status_text: str,
        headers: dict | None = None,
        body: str | None = None,
    ) -> None:
        self.text = f"{verson} {status_code} {status_text}"
        if headers is not None:
            self.text += "\n"
            for key, value in headers.items():
                self.text += f"{key}: {value}\n"
            self.text += "\n"
        if body is not None:
            if headers is not None:
                self.text = self.text.removesuffix("\n\n")
            self.text += f"\nContent-Length: {len(body)}\nContent-Type: text/html; charset=utf-8\n\n{body}"
