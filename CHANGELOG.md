# Changelog

## [0.1.3] - 2025-09-12
### Added
- Documentação atualizada em **Português (PT-BR)** e **English (EN)** (README completo, quickstart e guia de contribuição).
- Exemplos prontos em `examples/` (ex.: geração de badge básico).
- Suíte de testes automatizados (unittest/pytest) cobrindo `Model`, `Builder`, `engines/pillow` e `build_results`.
- Instruções para execução de testes e sugestões para CI e `pytest.ini`.

### Changed
- `Model._pages`: removido o default mutável; agora usa `default_factory=dict` (ou equivalente) para evitar compartilhamento entre instâncias.
- `Model.get_form()`: iteração corrigida para iterar objetos `Page` / seus campos (em vez de iterar chaves do dict).
- `Builder`: melhoria nas mensagens de erro e integração mais clara com engines (melhor tratamento de retorno de `engine.build_result()`).
- `BuildResult`: comportamento de `to_bytes()` documentado/clarificado; `save()` melhor tratado para caminhos de ficheiro x diretórios e para múltiplas páginas.

### Fixed
- Engine Pillow:
  - Abre imagens com `Image.open(...).convert("RGBA")` para garantir modos consistentes.
  - Usa `paste(..., mask=...)` quando necessário para preservar canal alfa/transparência.
  - Fallback para fonte corrigido (não usar `ImageFont.load_default(size=...)`, garantir fallback válido).
- Evitar exceções com mensagens vazias; mensagens de erro agora são descritivas.
- Correções diversas de robustez (validações de dimensão/background em `PillowMotor.new_page`, tratamento de entradas vazias em `ImageBuildResult`).

### Documentation & Tests
- README bilíngue (PT/EN) com quickstart, API summary e boas práticas.
- Testes adicionados com instruções de execução (`pytest` / `python -m unittest`).
- Exemplos que demonstram `render().show()`, `save()` (arquivo e diretório) e exportação multi-página.

### Notes
- Não são esperadas breaking changes para usuários finais; algumas melhorias internas podem afetar serialização/instâncias se você dependia de `_pages` como atributo mutável por referência.

## [0.1.2] - 2025-09-11
### Fixed
- Fixando bugs

## [0.1.1] - 2025-09-11
### Added
- Ajuste ao buildar um formulário a partir do modelo
- Builder podendo construir images com pillow ou pdf com reportlib
- Adicionado `CHANGELOG.md`.

### Fixed
- Correção no get e setter dos componentes
- Mudança de add_field para add_component

## [0.1.0] - 2025-09-10
### Added
- Primeira versão publicada da lib.
