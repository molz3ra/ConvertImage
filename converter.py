import os
from PIL import Image

# --- Configuração ---
pasta_entrada = 'entrada'
pasta_saida = 'saida'
formatos_entrada = ('.png', '.webp')
formato_saida_ext = '.jpg'
formato_saida_pil = 'JPEG'
qualidade_jpg = 85  
# --------------------

# 1. Cria a pasta de saída se não existir
os.makedirs(pasta_saida, exist_ok=True)

print(f"Iniciando conversão... Lendo de '{pasta_entrada}', salvando em '{pasta_saida}'")

# 2. Itera sobre os arquivos na pasta de entrada
for nome_arquivo in os.listdir(pasta_entrada):
    # Checa se o arquivo tem uma das extensões desejadas
    if nome_arquivo.lower().endswith(formatos_entrada):
        
        # 3. Monta o caminho completo de entrada e saída
        caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
        
        # Remove a extensão antiga (.png ou .webp) e adiciona a nova (.jpg)
        nome_base = os.path.splitext(nome_arquivo)[0]
        novo_nome = nome_base + formato_saida_ext
        caminho_saida = os.path.join(pasta_saida, novo_nome)

        try:
            # 4. Abre a imagem (A mágica do Pillow começa aqui)
            with Image.open(caminho_entrada) as img:
                
                # 5. CONVERSÃO CRUCIAL:
                #    .jpg não suporta transparência (canal Alpha/RGBA).
                #    Precisamos converter a imagem para o modo 'RGB' antes de salvar.
                #    Isso adiciona um fundo branco (por padrão) onde era transparente.
                if img.mode == 'RGBA' or img.mode == 'P': # 'P' é paleta, pode ter transparência
                    img_convertida = img.convert('RGB')
                else:
                    img_convertida = img

                # 6. Salva a imagem no novo formato (A mágica termina aqui)
                img_convertida.save(caminho_saida, formato_saida_pil, quality=qualidade_jpg)
                
                print(f"[SUCESSO] Convertido: {nome_arquivo} -> {novo_nome}")

        except Exception as e:
            print(f"[ERRO] Falha ao converter {nome_arquivo}: {e}")

print("Conversão concluída!")