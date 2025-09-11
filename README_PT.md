# Imprint

**Imprint** é uma biblioteca Python para criar e gerar modelos de documentos visuais, como certificados, crachás, convites e outros templates gráficos, de forma simples e programática. Ela permite preencher campos dinâmicos a partir de APIs, arquivos Excel, banco de dados ou qualquer fonte de dados.

---

## ⚡ Recursos

* Criação de **modelos** personalizados com múltiplas páginas.
* Adição de **campos dinâmicos**: textos, imagens e QR codes.
* Definição de **tamanho e posição** de campos em cada página.
* Exportação de modelos para **imagens PNG** ou outros formatos.
* Integração fácil com **APIs, Excel e bancos de dados**.
* Estrutura modular para extensões futuras (novos tipos de campos e efeitos gráficos).

---

## 🚀 Instalação

Você pode instalar diretamente do repositório (quando disponível no PyPI, basta substituir `git+...` por `pip install imprint`):

```bash
pip install git+https://github.com/seu-usuario/imprint.git
```

---

## 📝 Exemplo de uso básico

```python
import os
from imprint import Model

def criar_modelo_cracha():
    caminho_fundo = os.path.join(os.getcwd(), "examples/assets/cracha.png")

    modelo = Model.new(name="Cracha-Basico")

    pagina_frente = modelo.new_page(name="frente")
    pagina_frente.set_background(caminho_fundo)

    campo_nome = pagina_frente.add_component(name="Nome completo", component="text", form_key="name")
    campo_nome.set_position((520, 320))
    campo_nome.set_size(24)

    campo_cargo = pagina_frente.add_component(name="Cargo", component="text", form_key="job")
    campo_cargo.set_position((510, 400))
    campo_cargo.set_size(24)

    campo_acesso = pagina_frente.add_component(name="Nível de acesso", component="text", form_key="role")
    campo_acesso.set_position((610, 480))
    campo_acesso.set_size(24)

    campo_foto = pagina_frente.add_component(name="Foto", component="img", form_key="photo")
    campo_foto.set_position((35, 245))
    campo_foto.set_dimension((360, 360))

    return modelo

modelo = criar_modelo_cracha()

formulario = {
    "name": "Daniel Fernandes Pereira",
    "job": "Desenvolvedor de Software",
    "role": "Administrador",
    "photo": os.path.join(os.getcwd(), "examples/assets/foto.png")
}

resultado = modelo.build(formulario).make_images()
# para visualizar
resultado.show()
# para salvar
resultado.save("resultado.png", format="PNG")

# Multiplas páginas
resultados = modelo.build(formulario).make_images()
for i, pagina in enumerate(resultados):
    pagina.save(f"resultado-{i}.png", format="PNG")
```

---

## 🔧 Estrutura do modelo

* **Model**: representa o documento completo, contendo múltiplas páginas.
* **Page**: representa cada página do modelo.
* **Field**: representa os campos dinâmicos que podem ser preenchidos (texto, imagem, QR code, etc.).
* **Components**: conjunto de tipos de campos disponíveis.

---

## 🌟 Próximos recursos planejados

* Suporte a **camadas e efeitos visuais**.
* Exportação em **PDF** diretamente.
* Integração com **planilhas Excel** e arquivos CSV.
* Suporte a **QR codes dinâmicos** e códigos de barras.
* Templates compartilháveis via **API**.

---

## 💡 Contribuindo

1. **Faça um fork** do projeto.
2. **Crie uma branch** para sua feature:

```bash
git checkout -b feature/nova-funcionalidade
```

---

## 📄 Licença

MIT License © Daniel Fernandes
