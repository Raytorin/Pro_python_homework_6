import requests


class YaCreateFolder:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def create_folder(self, disk_file_path):
        create_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.put(create_url, headers=headers, params=params)
        return response

    def delete_folder(self, disk_file_path):
        url_delete = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers_delete = self.get_headers()
        params_delete = {"path": disk_file_path, "permanently": "true"}
        resource = requests.delete(url_delete, headers=headers_delete, params=params_delete)
        return resource


if __name__ == '__main__':
    token_ya = ''
    folder_ya = YaCreateFolder(token_ya)
    path = 'new_folder'
    result_create = folder_ya.create_folder(path)
    print(result_create)
    result_delete = folder_ya.delete_folder(path)
    print(result_delete)
