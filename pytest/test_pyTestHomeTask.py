import pytest


from pyTestHomeTask import get_languages

# Функция для тестирования популярности языков программирования
@pytest.mark.parametrize("popularity", [10**7, 1.5*10**7, 5*10**7, 10**8, 5*10**8, 10**9, 1.5*10**9])
def test_popularity(popularity):
    languages = get_languages()
    errors = []
    for language in languages:
        if language.popularity < popularity:
            # Создает ошибку при 'Меньше' стейтменте
            error_message = f"{language.name} (Frontend:{language.category_front}|Backend:{language.category_back}) has {language.popularity} unique visitors per month. (Expected more than {popularity})"
            errors.append(error_message)
    # Выводим ошибку с коллекцией выше собранных ошибок
    assert not errors, "\n".join(errors)