import pytest
from yandex_disk import YaCreateFolder


token = ""

FIXTURE1 = [(token, "new_folder", "201")]

FIXTURE2 = [(token, "new_folder", "204")]


@pytest.mark.parametrize("token_ya, path, status_code_1", FIXTURE1)
def test_create_folder_ya(token_ya, path, status_code_1):
    folder_ya = YaCreateFolder(token_ya)
    result_create = str(folder_ya.create_folder(path).status_code)
    assert result_create == status_code_1, 'Папка успешно создана'


@pytest.mark.parametrize("token_ya, path, status_code_2", FIXTURE2)
def test_delete_folder_ya(token_ya, path, status_code_2):
    folder_ya = YaCreateFolder(token_ya)
    result_delete = str(folder_ya.delete_folder(path).status_code)
    assert result_delete == status_code_2, 'Папка успешно удалена'
