import json
import sys
from pathlib import Path
from urllib.parse import urlparse

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QStyle,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtWebEngineWidgets import QWebEngineView

CONFIG_DIR = Path.home() / ".haddock-browser"
CONFIG_FILE = CONFIG_DIR / "settings.json"


def normalize_url(text: str) -> QUrl:
    """
    Transforme ce que l'utilisateur tape en URL exploitable :
    - si vide -> about:blank
    - si pas de schema (http/https) -> on ajoute https://
    """
    raw = (text or "").strip()
    if not raw:
        return QUrl("about:blank")

    parsed = urlparse(raw)
    if not parsed.scheme:
        raw = "https://" + raw

    return QUrl(raw)


def load_settings() -> dict:
    defaults = {
        "startup_url": "https://www.example.com",
        "home_url": "https://www.example.com",
    }
    try:
        if CONFIG_FILE.exists():
            data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
            for key in list(defaults.keys()):
                value = data.get(key)
                if isinstance(value, str) and value.strip():
                    defaults[key] = value.strip()
    except Exception:
        pass
    return defaults


def save_settings(settings: dict) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(settings, indent=2), encoding="utf-8")


class SettingsDialog(QDialog):
    def __init__(self, parent: QWidget, startup_url: str, home_url: str) -> None:
        super().__init__(parent)
        self.setWindowTitle("Parametres")

        self.startup_input = QLineEdit(startup_url)
        self.home_input = QLineEdit(home_url)

        form = QFormLayout()
        form.addRow("Page de demarrage", self.startup_input)
        form.addRow("Page d'accueil", self.home_input)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        root = QVBoxLayout()
        root.addLayout(form)
        root.addWidget(buttons)
        self.setLayout(root)

    def values(self) -> tuple[str, str]:
        return (self.startup_input.text().strip(), self.home_input.text().strip())


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Navigateur Haddock - v3")
        self.resize(1100, 700)

        # Widgets
        self.settings = load_settings()
        self.address_bar = QLineEdit()
        self.address_bar.setPlaceholderText("Entrez une adresse (ex: wikipedia.org)")

        self.back_button = QPushButton("Retour")
        self.forward_button = QPushButton("Avance")
        self.reload_button = QPushButton("Recharger")
        self.home_button = QPushButton("Accueil")
        self.go_button = QPushButton("Aller")
        self.settings_button = QPushButton("Parametres")
        self.web_view = QWebEngineView()

        style = self.style()
        self.back_button.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_ArrowBack))
        self.forward_button.setIcon(
            style.standardIcon(QStyle.StandardPixmap.SP_ArrowForward)
        )
        self.reload_button.setIcon(
            style.standardIcon(QStyle.StandardPixmap.SP_BrowserReload)
        )
        self.home_button.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_DirHomeIcon))
        self.go_button.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_CommandLink))
        self.settings_button.setIcon(
            style.standardIcon(QStyle.StandardPixmap.SP_TitleBarMenuButton)
        )

        # Layout top bar
        top_bar = QHBoxLayout()
        top_bar.addWidget(self.back_button)
        top_bar.addWidget(self.forward_button)
        top_bar.addWidget(self.reload_button)
        top_bar.addWidget(self.home_button)
        top_bar.addWidget(self.address_bar, stretch=1)
        top_bar.addWidget(self.go_button)
        top_bar.addWidget(self.settings_button)

        # Layout principal
        root = QVBoxLayout()
        root.addLayout(top_bar)
        root.addWidget(self.web_view, stretch=1)

        container = QWidget()
        container.setLayout(root)
        self.setCentralWidget(container)

        # Connexions (signaux)
        self.back_button.clicked.connect(self.web_view.back)
        self.forward_button.clicked.connect(self.web_view.forward)
        self.reload_button.clicked.connect(self.web_view.reload)
        self.home_button.clicked.connect(self.go_home)
        self.go_button.clicked.connect(self.go_to_address)
        self.address_bar.returnPressed.connect(self.go_to_address)
        self.web_view.urlChanged.connect(self.sync_address_bar)
        self.settings_button.clicked.connect(self.open_settings)

        # Page par defaut (optionnel)
        self.web_view.setUrl(normalize_url(self.settings["startup_url"]))

    def go_to_address(self) -> None:
        url = normalize_url(self.address_bar.text())
        self.web_view.setUrl(url)

    def sync_address_bar(self, url: QUrl) -> None:
        self.address_bar.setText(url.toString())

    def go_home(self) -> None:
        self.web_view.setUrl(normalize_url(self.settings["home_url"]))

    def open_settings(self) -> None:
        dialog = SettingsDialog(
            self, self.settings["startup_url"], self.settings["home_url"]
        )
        if dialog.exec():
            startup_url, home_url = dialog.values()
            if startup_url:
                self.settings["startup_url"] = startup_url
            if home_url:
                self.settings["home_url"] = home_url
            save_settings(self.settings)


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
