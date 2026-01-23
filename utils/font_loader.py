from typing import List

from PySide6.QtGui import QFontDatabase, QFont

from utils.path_helper import resource_path


def load_app_fonts() -> List[str]:
    fonts_dir = resource_path("fonts")
    loaded_families: List[str] = []
    if not fonts_dir.exists():
        return loaded_families

    for font_path in fonts_dir.glob("*.ttf"):
        font_id = QFontDatabase.addApplicationFont(str(font_path))
        if font_id != -1:
            loaded_families.extend(QFontDatabase.applicationFontFamilies(font_id))

    for font_path in fonts_dir.glob("*.otf"):
        font_id = QFontDatabase.addApplicationFont(str(font_path))
        if font_id != -1:
            loaded_families.extend(QFontDatabase.applicationFontFamilies(font_id))

    return loaded_families


def apply_first_font(app, families: List[str]) -> None:
    if families:
        app.setFont(QFont(families[0]))
