import os
import subprocess
import sys

def check_environment():
    """Проверяет, что скрипт запущен в правильной виртуальной среде."""
    # Получаем путь к текущей виртуальной среде
    virtual_env = os.environ.get('VIRTUAL_ENV')
    if virtual_env is None:
        raise Exception("Скрипт не запущен в виртуальной среде!")

    # Проверяем, что имя виртуальной среды соответствует ожидаемому
    expected_env_name = "naysswyf"
    if expected_env_name not in virtual_env:
        raise Exception(f"Скрипт запущен не в той виртуальной среде! Ожидалось: {expected_env_name}")

def install_requirements():
    """Устанавливает библиотеки из файла requirements.txt."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        raise Exception(f"Ошибка при установке библиотек: {e}")

def list_installed_packages():
    """Возвращает список установленных библиотек в формате 'name==version'."""
    result = subprocess.run(
        [sys.executable, "-m", "pip", "freeze"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f"Ошибка при получении списка установленных библиотек: {result.stderr}")
    return result.stdout.strip().split("\n")

def save_requirements(packages):
    """Сохраняет список установленных библиотек в файл requirements.txt."""
    with open("requirements.txt", "w") as file:
        file.write("\n".join(packages))

def archive_env():
    """Архивирует виртуальную среду в папку env_path/ex02/src."""
    env_path = os.environ.get('VIRTUAL_ENV')
    if env_path is None:
        raise Exception("Виртуальная среда не найдена!")

    # Путь для сохранения архива
    archive_dir = os.path.join(os.path.dirname(env_path), "ex02", "src")
    os.makedirs(archive_dir, exist_ok=True)

    # Имя архива
    archive_name = f"{os.path.basename(env_path)}.tar.gz"
    archive_path = os.path.join(archive_dir, archive_name)

    # Создаем архив
    subprocess.run(["tar", "-czvf", archive_path, "-C", os.path.dirname(env_path), os.path.basename(env_path)])
    print(f"Виртуальная среда архивирована в {archive_path}")

def main():
    # Проверяем, что скрипт запущен в правильной среде
    check_environment()

    # Устанавливаем библиотеки
    install_requirements()

    # Получаем список установленных библиотек
    installed_packages = list_installed_packages()

    # Отображаем установленные библиотеки
    print("Установленные библиотеки:")
    for package in installed_packages:
        print(package)

    # Сохраняем список установленных библиотек в requirements.txt
    save_requirements(installed_packages)

    # Архивируем виртуальную среду
    archive_env()

if __name__ == "__main__":
    main()
