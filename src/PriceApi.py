class PublicApi:
    def getPrice(self, id):
        raise ConnectionError(f"Failed to get price for {id}")
