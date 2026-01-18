import sys
from urllib.parse import urlparse

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtWebEngineWidgets import QWebEngineView


def normalize_url(text: str) -> QUrl:
    """
    Transforme ce que l'utilisateur tape en URL exploitable :
    - si vide -> about:blank
    - si pas de schéma (http/https) -> on ajoute https://
    """
    raw = (text or "").strip()
    if not raw:
        return QUrl("about:blank")

    parsed = urlparse(raw)
    if not parsed.scheme:
        raw = "https://" + raw

    return QUrl(raw)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Navigateur Haddock - v2")
        self.resize(1100, 700)

        # Widgets
        self.address_bar = QLineEdit()
        self.address_bar.setPlaceholderText("Entrez une adresse (ex: wikipedia.org)")

        self.back_button = QPushButton("Retour")
        self.forward_button = QPushButton("Avance")
        self.reload_button = QPushButton("Recharger")
        self.go_button = QPushButton("Aller")
        self.web_view = QWebEngineView()

        # Layout top bar
        top_bar = QHBoxLayout()
        top_bar.addWidget(self.back_button)
        top_bar.addWidget(self.forward_button)
        top_bar.addWidget(self.reload_button)
        top_bar.addWidget(self.address_bar, stretch=1)
        top_bar.addWidget(self.go_button)

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
        self.go_button.clicked.connect(self.go_to_address)
        self.address_bar.returnPressed.connect(self.go_to_address)
        self.web_view.urlChanged.connect(self.sync_address_bar)

        # Page par défaut (optionnel)
        self.web_view.setUrl(QUrl("https://www.example.com"))

    def go_to_address(self) -> None:
        url = normalize_url(self.address_bar.text())
        self.web_view.setUrl(url)

    def sync_address_bar(self, url: QUrl) -> None:
        self.address_bar.setText(url.toString())


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
