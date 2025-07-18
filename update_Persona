import pygame
import random
import sys
import os
from pygame.locals import *
import pickle

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gerador de Personagens - Crônicas dos Personagens")

# Cores no tema pergaminho antigo
PARCHMENT = (240, 230, 200)  # Cor base do pergaminho
PARCHMENT_DARK = (200, 190, 160)  # Tons mais escuros para contrastes
PARCHMENT_STAIN = (220, 210, 170)  # Manchas de envelhecimento
INK_BROWN = (70, 50, 20)  # Cor de tinta marrom (em vez de preto)
INK_LIGHT = (100, 80, 50)  # Tinta desbotada
STAIN_MOLD = (180, 190, 150)  # Tons de mofo/umidade
BUTTON_AGED = (160, 140, 100)  # Botões envelhecidos
BUTTON_HIGHLIGHT = (180, 160, 120)  # Botões com destaque
WHITE = (255, 255, 255)  # Branco puro para alguns elementos

# Carrega fonte pixel art (substitua pelo caminho da sua fonte ou use uma padrão)
try:
    # Tenta carregar uma fonte pixel art (você precisa ter o arquivo .ttf)
    pixel_font = pygame.font.Font("fonts\pixel_operator\PixelOperator.ttf", 16)
    pixel_font_large = pygame.font.Font("fonts\pixel_operator\PixelOperator.ttf", 24)
    pixel_font_title = pygame.font.Font("fonts\pixel_operator\PixelOperator.ttf", 32)
except:
    # Fallback para fonte padrão se a pixel art não estiver disponível
    print("Fonte pixel art não encontrada, usando fonte padrão")
    pixel_font = pygame.font.SysFont('Courier New', 16, bold=True)
    pixel_font_large = pygame.font.SysFont('Courier New', 24, bold=True)
    pixel_font_title = pygame.font.SysFont('Courier New', 32, bold=True)

# Listas de nomes masculinos
male_names = [
    "João", "Pedro", "Carlos", "Miguel", "Rafael", "Antônio", "Fernando", 
    "Ricardo", "Gustavo", "Eduardo", "Marcos", "Lucas", "Daniel", "Paulo",
    "John", "James", "Robert", "Michael", "William", "David", "Joseph", 
    "Matthew", "Christopher", "Andrew", "Edward", "Hans", "Klaus", "Wolfgang",
    "Dieter", "Friedrich", "Heinrich", "Johann", "Karl", "Stefan", "Thomas"
]

# Listas de nomes femininos
female_names = [
    "Maria", "Ana", "Lucia", "Sofia", "Isabella", "Laura", "Beatriz", 
    "Camila", "Amanda", "Juliana", "Carolina", "Patrícia", "Fernanda", "Raquel",
    "Mary", "Emma", "Olivia", "Sophia", "Ava", "Mia", "Charlotte", "Amelia",
    "Elizabeth", "Margaret", "Emily", "Victoria", "Greta", "Ingrid", "Helga",
    "Ursula", "Elsa", "Marta", "Anneliese", "Clara", "Hannah", "Lena"
]

# Sobrenomes por classe social
noble_surnames = ["Adnor", "Frokz", "Stentyrm", "Vrikz", "Elslinir", "Rotavsk", "Cronas", "Brunks", "Sylens"]
common_surnames = ["Rosters", "Bonglers", "Mklaver", "Drawnd", "Foilty"]
dark_surnames = ["Blonkis", "Grwannir", "Duwnm", "Honsto", "Gwalner", "Vrowntan", "Delins"]

# Detalhes únicos dos personagens
unique_details = [
    "Sempre está cheirando a cigarro", "Anda com um crucifixo que tem um guarda-foto",
    "Está sempre comendo doces", "Sempre escrevendo algo em um caderno ou lendo",
    "Tem o hábito de tamborilar os dedos quando pensa", "Sempre arruma os óculos a cada 2 minutos",
    "Tem um lenço bordado que nunca usa, só fica olhando", "Canta baixinho quando está concentrado",
    "Tem um relógio de bolso que nunca funciona", "Sempre anda com um guarda-chuva, mesmo em dias ensolarados",
    "Sempre cumprimenta desconhecidos como se os conhecesse", "Tem um caderno cheio de anotações estranhas",
    "Bate na madeira três vezes ao ouvir algo azarado", "Sempre confunde ‘esquerda’ e ‘direita’ e precisa olhar para as mãos",
    "Guarda recibo de tudo, até de bala", "só não esquece a cabeça, de resto, esquece tudo",
    "desorganizado", "egocentrico", "sempre fala sozinho", "tem medo de escuro", "tem medo de altura",
    "gosta de fazer o caos", "gosta de animais", "gosta de plantas", "gosta de tecnologia", "pidão", "exagerado",
    "não tem como definir, ele se supera a cada dia", "tem lingua presa, mas fala que é sotaque (melhor não rir disso)"
]

class CharacterManager:
    def __init__(self):
        self.favorites = []
        self.load_favorites()
    
    def load_favorites(self):
        """Carrega os favoritos de um arquivo"""
        try:
            with open("favorites.dat", "rb") as f:
                self.favorites = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.favorites = []
    
    def save_favorites(self):
        """Salva os favoritos em um arquivo"""
        with open("favorites.dat", "wb") as f:
            pickle.dump(self.favorites, f)
    
    def add_favorite(self, character):
        """Adiciona um personagem aos favoritos"""
        # Verifica se já não está nos favoritos
        if not any(fav.get_full_name() == character.get_full_name() for fav in self.favorites):
            self.favorites.append(character)
            self.save_favorites()
    
    def remove_favorite(self, character):
        """Remove um personagem dos favoritos"""
        # Remove por nome completo
        self.favorites = [fav for fav in self.favorites 
                         if fav.get_full_name() != character.get_full_name()]
        self.save_favorites()
    
    def is_favorite(self, character):
        """Verifica se um personagem é favorito"""
        return any(fav.get_full_name() == character.get_full_name() 
                  for fav in self.favorites)

class Character:
    def __init__(self):
        """Inicializa um novo personagem com atributos aleatórios"""
        self.generate()
        self.editing = False  # Modo de edição
        self.edit_field = None  # Campo sendo editado atualmente

    def generate_birth_date(self):
        """Gera uma data de nascimento aleatória"""
        year = random.randint(1950, 2005)
        month = random.randint(1, 12)
        # Garante que o dia é válido para o mês (não considera anos bissextos para simplificar)
        if month == 2:
            day = random.randint(1, 28)
        elif month in [4, 6, 9, 11]:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)
    
        return f"{day:02d}/{month:02d}/{year}"
    
    def generate(self):
        """Gera atributos aleatórios para o personagem"""
        # Gênero
        self.gender = random.choice(["Masculino", "Feminino"])
        
        # Nome conforme gênero
        if self.gender == "Masculino":
            self.first_name = random.choice(male_names)
        else:
            self.first_name = random.choice(female_names)
        
            # Data de nascimento
        self.birth_date = self.generate_birth_date()

        # Raça
        self.race = random.choice(["Humano", "Demônio", "Anjo", "Feiticeiro", "Cientista", "Vazio"])
        
        # Características físicas
        self.hair_color = random.choice(["Preto", "Castanho", "Loiro", "Ruivo", "Cinza", "Branco", "Colorido"])
        self.eye_color = random.choice(["Azul", "Verde", "Castanho", "Preto", "Cinza", "Vermelho", "Âmbar"])
        self.height = random.randint(150, 200)
        
        # Cicatriz da raça
        self.scar = self.generate_scar()
        
        # Classe/Profissão
        self.profession = random.choice([
            "Ladrão", "Assassino", "Agente", "Trabalhador", "Viajante", "Comerciante", 
            "Empresário", "Jornalista", "Enfermeiro", "Curandeiro", "Rico", "Químico", 
            "Criacionista", "Ocultista"
        ])
        
        # Personalidade / Caráter
        self.personality = random.choice([
            "Bravo", "Alegre", "Sério", "Tímido", "Extrovertido", "Sábio", "Ingênuo", 
            "Cínico", "Leal", "Trapaceiro", "Misterioso", "Melancólico", "Entusiasta", "Calculista"
        ])
        
        # Origem/História
        self.background = random.choice([
            "Celestial", "Nobre", "Rico", "Centro", "Interior Rural", "Florestal", "Fendas", "Nulo"
        ])
        
        # Sobrenome baseado na origem
        if self.background in ["Celestial", "Nobre", "Rico"]:
            self.surname = random.choice(noble_surnames)
        elif self.background in ["Fendas", "Nulo"]:
            self.surname = random.choice(dark_surnames)
        else:
            self.surname = random.choice(common_surnames)
        
        # Detalhe único
        self.unique_detail = random.choice(unique_details)
    
    def generate_scar(self):
        """Retorna a cicatriz característica da raça"""
        scars = {
            "Humano": "Cicatriz de queimadura na palma da mão",
            "Demônio": "Marca de garra na parte interna do pulso",
            "Anjo": "Símbolo luminoso no dorso da mão",
            "Feiticeiro": "Padrão geométrico entre os dedos",
            "Cientista": "Cicatriz cirúrgica ao longo da linha da vida",
            "Vazio": "Pele levemente translúcida nas articulações"
        }
        return scars.get(self.race, "Cicatriz desconhecida")

    def get_full_name(self):
        """Retorna o nome completo do personagem"""
        return f"{self.first_name} {self.surname}"
    
    def save_to_file(self, filename):
        """Salva os dados do personagem em um arquivo na área de trabalho"""
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        filepath = os.path.join(desktop, filename)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(f"Nome: {self.get_full_name()}\n")
            file.write(f"Raça: {self.race}\n")
            file.write(f"Gênero: {self.gender}\n")
            file.write(f"Data de Nascimento: {self.birth_date}\n")
            file.write(f"Altura: {self.height}cm\n")
            file.write(f"Cabelo: {self.hair_color}\n")
            file.write(f"Olhos: {self.eye_color}\n")
            file.write(f"Cicatriz: {self.scar}\n")
            file.write(f"Classe: {self.profession}\n")
            file.write(f"Caráter: {self.personality}\n")
            file.write(f"Origem: {self.background}\n")
            file.write(f"Detalhe único: {self.unique_detail}\n\n")

def draw_button(screen, x, y, width, height, color, text, text_color=INK_BROWN):
    """Desenha um botão na tela e retorna seu retângulo de colisão"""
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=5)
    pygame.draw.rect(screen, INK_BROWN, (x, y, width, height), 2, border_radius=5)
    btn_text = pixel_font.render(text, True, text_color)
    screen.blit(btn_text, (x + width//2 - btn_text.get_width()//2, y + height//2 - btn_text.get_height()//2))
    return pygame.Rect(x, y, width, height)

def draw_text_field(screen, x, y, width, height, text, active=False):
    """Desenha um campo de texto editável"""
    color = BUTTON_HIGHLIGHT if active else PARCHMENT_DARK
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.draw.rect(screen, INK_BROWN, (x, y, width, height), 2)

    text_surface = pixel_font.render(text, True, INK_BROWN)
    # Trunca o texto se for muito longo
    if text_surface.get_width() > width - 10:
        text_surface = pixel_font.render(text[-20:], True, INK_BROWN)
    screen.blit(text_surface, (x + 5, y + 5))

def draw_character_sheet(screen, character, current_index, total_characters, char_manager):
    """Desenha a ficha completa do personagem"""
    # Fundo com textura de pergaminho
    screen.fill(PARCHMENT)
    
    
    # Título
    title = pixel_font_title.render("Crônicas dos Personagens", True, INK_BROWN)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 15))
    
    # Contador de personagens
    counter = pixel_font.render(f"Pergaminho {current_index + 1} de {total_characters}", True, INK_LIGHT)
    screen.blit(counter, (WIDTH//2 - counter.get_width()//2, 60))
    
    # Nome completo
    name = pixel_font_large.render(character.get_full_name(), True, INK_BROWN)
    screen.blit(name, (WIDTH//2 - name.get_width()//2, 100))
    
    # Área principal de informações
    y_offset = 150
    
    # Desenha o "papel" principal
    main_rect = pygame.Rect(50, 140, WIDTH - 100, HEIGHT - 250)
    pygame.draw.rect(screen, PARCHMENT_DARK, main_rect)
    pygame.draw.rect(screen, INK_BROWN, main_rect, 2)
    
    # Lista de campos editáveis
    fields = [
        ("Nome", character.first_name, "first_name"),
        ("Sobrenome", character.surname, "surname"),
        ("Nascimento", character.birth_date, "birth_date"),
        ("Raça", character.race, "race"),
        ("Gênero", character.gender, "gender"),
        ("Altura", f"{character.height}cm", "height"),
        ("Cabelo", character.hair_color, "hair_color"),
        ("Olhos", character.eye_color, "eye_color"),
        ("Cicatriz", character.scar, "scar"),
        ("Classe", character.profession, "profession"),
        ("Caráter", character.personality, "personality"),
        ("Origem", character.background, "background"),
        ("Detalhe", character.unique_detail, "unique_detail")
    ]
    
    # Desenha os campos
    field_rects = {}
    for i, (label, value, field_name) in enumerate(fields):
        # Label
        label_text = pixel_font.render(f"{label}: ", True, INK_BROWN)
        screen.blit(label_text, (70, y_offset + i*30))
        
        # Campo de valor (editável se estiver no modo de edição)
        if character.editing and character.edit_field == field_name:
            draw_text_field(screen, 200, y_offset + i*30 - 3, 300, 25, str(value), True)
            field_rects[field_name] = pygame.Rect(200, y_offset + i*30 - 3, 300, 25)
        else:
            value_text = pixel_font.render(str(value), True, INK_BROWN)
            screen.blit(value_text, (200, y_offset + i*30))
            field_rects[field_name] = pygame.Rect(200, y_offset + i*30 - 3, value_text.get_width(), 25)
    
    # Botões
    btn_new = draw_button(screen, 50, HEIGHT - 80, 150, 40, BUTTON_AGED, "Novo")
    btn_save = draw_button(screen, 220, HEIGHT - 80, 150, 40, BUTTON_AGED, "Salvar")
    btn_edit = draw_button(screen, 390, HEIGHT - 80, 150, 40, BUTTON_AGED, 
                          "Editar" if not character.editing else "Confirmar")
    btn_back = draw_button(screen, 560, HEIGHT - 80, 150, 40, BUTTON_AGED, "Voltar")
    btn_export = draw_button(screen, 730, HEIGHT - 80, 150, 40, BUTTON_AGED, "Exportar")
    
    # Novo botão de favorito
    fav_color = BUTTON_HIGHLIGHT if char_manager.is_favorite(character) else BUTTON_AGED
    btn_favorite = draw_button(screen, WIDTH//2 - 75, HEIGHT - 130, 150, 40, fav_color, 
                             "remover favorito" if char_manager.is_favorite(character) else "favoritar")
    
    return btn_new, btn_save, btn_edit, btn_back, btn_export, btn_favorite, field_rects

def number_selection_screen():
    """Tela de seleção de quantidade de personagens"""
    while True:  # Adicionamos um loop para manter a tela
        screen.fill(PARCHMENT)
        
        # Adiciona manchas de envelhecimento
        # Manchas de envelhecimento fixas (imóveis)
        stains = [
            (120, 180, 35),
            (700, 120, 45),
            (400, 400, 30),
            (250, 550, 40),
            (800, 600, 25)
        ]
        for x, y, r in stains:
            pygame.draw.circle(screen, PARCHMENT_STAIN, (x, y), r)
        
        title = pixel_font_title.render("Quantos personagens deseja gerar?", True, INK_BROWN)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
        
        buttons = []
        for i, num in enumerate([1, 3, 5, 10]):
            btn = draw_button(screen, WIDTH//2 - 150 + (i % 2) * 160, 200 + (i // 2) * 60, 140, 50, BUTTON_AGED, str(num))
            buttons.append((btn, num))
        
        # Adiciona o botão Voltar
        btn_back = draw_button(screen, WIDTH//2 - 75, 350, 150, 40, BUTTON_AGED, "Voltar")
        
        pygame.display.flip()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if btn_back.collidepoint(mouse_pos):
                    return None, True  # Retorna None e True (indicando que quer voltar)
                
                for btn, num in buttons:
                    if btn.collidepoint(mouse_pos):
                        return num, False  # Retorna o número e False (não quer voltar)

def character_generation_screen(num_characters, char_manager):
    """Tela principal de geração e edição de personagens"""
    characters = [Character() for _ in range(num_characters)]
    current_character = 0
    
    clock = pygame.time.Clock()
    input_text = ""
    
    
    while True:
        btn_new, btn_save, btn_edit, btn_back, btn_export, btn_favorite, fields = draw_character_sheet(
            screen, characters[current_character], current_character, num_characters, char_manager)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if btn_new.collidepoint(mouse_pos):
                    characters[current_character] = Character()
                
                elif btn_favorite.collidepoint(mouse_pos):
                    if char_manager.is_favorite(characters[current_character]):
                        char_manager.remove_favorite(characters[current_character])
                    else:
                        char_manager.add_favorite(characters[current_character])
                    
                elif btn_save.collidepoint(mouse_pos):
                    characters[current_character].editing = False
                
                elif btn_edit.collidepoint(mouse_pos):
                    if characters[current_character].editing:
                        # Sai do modo de edição
                        characters[current_character].editing = False
                    else:
                        # Entra no modo de edição
                        characters[current_character].editing = True
                        characters[current_character].edit_field = None
                
                elif btn_back.collidepoint(mouse_pos):
                    return True  # Indica que quer voltar
                
                elif btn_export.collidepoint(mouse_pos):
                    filename = f"Personagem_{characters[current_character].get_full_name()}.txt"
                    characters[current_character].save_to_file(filename)
                
                # Verifica clique nos campos quando em modo de edição
                if characters[current_character].editing:
                    for field_name, rect in fields.items():
                        if rect.collidepoint(mouse_pos):
                            characters[current_character].edit_field = field_name
                            # Prepara o texto atual para edição
                            if field_name == "height":
                                input_text = str(getattr(characters[current_character], field_name)).replace("cm", "")
                            else:
                                input_text = str(getattr(characters[current_character], field_name))
                            break
            
            elif event.type == KEYDOWN and characters[current_character].editing and characters[current_character].edit_field:
                if event.key == K_RETURN:
                    # Confirma a edição
                    setattr(characters[current_character], characters[current_character].edit_field, input_text)
                    characters[current_character].edit_field = None
                    input_text = ""
                elif event.key == K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
                
                # Atualiza o valor do campo sendo editado
                if characters[current_character].edit_field:
                    if characters[current_character].edit_field == "height":
                        setattr(characters[current_character], characters[current_character].edit_field, f"{input_text}cm")
                    else:
                        setattr(characters[current_character], characters[current_character].edit_field, input_text)
            
            # Navegação entre personagens
            if num_characters > 1:
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 20 <= mouse_pos[0] <= 50 and HEIGHT//2 - 15 <= mouse_pos[1] <= HEIGHT//2 + 15:
                        current_character = (current_character - 1) % num_characters
                    elif WIDTH - 50 <= mouse_pos[0] <= WIDTH - 20 and HEIGHT//2 - 15 <= mouse_pos[1] <= HEIGHT//2 + 15:
                        current_character = (current_character + 1) % num_characters
        
        # Desenha setas de navegação se houver múltiplos personagens
        if num_characters > 1:
            pygame.draw.polygon(screen, INK_BROWN, [(30, HEIGHT//2), (50, HEIGHT//2 - 15), (50, HEIGHT//2 + 15)])
            pygame.draw.polygon(screen, INK_BROWN, [(WIDTH - 30, HEIGHT//2), (WIDTH - 50, HEIGHT//2 - 15), (WIDTH - 50, HEIGHT//2 + 15)])
        
        pygame.display.flip()
        clock.tick(30)

def favorites_screen(char_manager):
    """Tela que mostra todos os personagens favoritos com opções de exportar e remover"""
    while True:
        screen.fill(PARCHMENT)
        
        title = pixel_font_title.render("Personagens Favoritos", True, INK_BROWN)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))
        
        if not char_manager.favorites:
            no_fav = pixel_font_large.render("Nenhum favorito ainda!", True, INK_LIGHT)
            screen.blit(no_fav, (WIDTH//2 - no_fav.get_width()//2, HEIGHT//2))
        else:
            char_rects = []  # Para armazenar os retângulos dos personagens
            export_rects = []  # Para armazenar os botões de exportar
            delete_rects = []  # Para armazenar os botões de remover
            
            for i, char in enumerate(char_manager.favorites):
                if i >= 8:  # Limita a quantidade mostrada
                    break
                
                y_position = 100 + i * 50
                
                # Desenha o nome do personagem
                char_text = pixel_font.render(f"{i+1}. {char.get_full_name()} - {char.race}", True, INK_BROWN)
                text_rect = screen.blit(char_text, (100, y_position))
                char_rects.append((text_rect, char))
                
                # Desenha botão de exportar
                btn_export = draw_button(screen, WIDTH - 280, y_position, 120, 30, BUTTON_AGED, "Exportar")
                export_rects.append((btn_export, char))
                
                # Desenha botão de remover
                btn_delete = draw_button(screen, WIDTH - 150, y_position, 120, 30, (200, 50, 50), "Remover")
                delete_rects.append((btn_delete, char))
        
        btn_back = draw_button(screen, WIDTH//2 - 75, HEIGHT - 80, 150, 40, BUTTON_AGED, "Voltar")
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if btn_back.collidepoint(mouse_pos):
                    return
                
                # Verifica se clicou em algum botão de exportar
                if 'export_rects' in locals():
                    for btn, char in export_rects:
                        if btn.collidepoint(mouse_pos):
                            filename = f"FAVORITO_{char.get_full_name()}.txt"
                            char.save_to_file(filename)
                            # Feedback visual
                            feedback = pixel_font.render(f"Exportado como {filename}", True, (0, 100, 0))
                            screen.blit(feedback, (WIDTH//2 - feedback.get_width()//2, HEIGHT - 120))
                            pygame.display.flip()
                            pygame.time.delay(1000)  # Mostra o feedback por 1 segundo
                            break
                
                # Verifica se clicou em algum botão de remoção
                if 'delete_rects' in locals():
                    for btn, char in delete_rects:
                        if btn.collidepoint(mouse_pos):
                            char_manager.remove_favorite(char)
                            pygame.time.delay(200)  # Pequeno delay para feedback
                            break
                
                # Verifica se clicou em algum personagem para visualizar
                if 'char_rects' in locals():
                    for rect, char in char_rects:
                        if rect.collidepoint(mouse_pos):
                            view_character_screen(char, char_manager)
                            break

def view_character_screen(character, char_manager):
    """Tela para visualizar um personagem específico com opções de exportar e remover"""
    while True:
        screen.fill(PARCHMENT)
        
        # Título
        title = pixel_font_title.render("Detalhes do Personagem", True, INK_BROWN)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))
        
        # Nome completo
        name = pixel_font_large.render(character.get_full_name(), True, INK_BROWN)
        screen.blit(name, (WIDTH//2 - name.get_width()//2, 80))
        
        # Área principal de informações
        y_offset = 130
        main_rect = pygame.Rect(50, 120, WIDTH - 100, HEIGHT - 220)
        pygame.draw.rect(screen, PARCHMENT_DARK, main_rect)
        pygame.draw.rect(screen, INK_BROWN, main_rect, 2)
        
        # Lista de atributos
        attributes = [
            ("Nascimento", character.birth_date),
            ("Raça", character.race),
            ("Gênero", character.gender),
            ("Nascimento", character.birth_date),
            ("Altura", f"{character.height}cm"),
            ("Cabelo", character.hair_color),
            ("Olhos", character.eye_color),
            ("Cicatriz", character.scar),
            ("Classe", character.profession),
            ("Caráter", character.personality),
            ("Origem", character.background),
            ("Detalhe único", character.unique_detail)
        ]
        
        for i, (label, value) in enumerate(attributes):
            label_text = pixel_font.render(f"{label}: ", True, INK_BROWN)
            screen.blit(label_text, (70, y_offset + i*30))
            
            value_text = pixel_font.render(str(value), True, INK_BROWN)
            screen.blit(value_text, (200, y_offset + i*30))
        
        # Botões
        btn_export = draw_button(screen, WIDTH//2 - 220, HEIGHT - 120, 200, 40, BUTTON_AGED, "Exportar")
        btn_remove = draw_button(screen, WIDTH//2 + 20, HEIGHT - 120, 200, 40, (200, 50, 50), "Remover Favorito")
        btn_back = draw_button(screen, WIDTH//2 - 75, HEIGHT - 70, 150, 40, BUTTON_AGED, "Voltar")
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if btn_back.collidepoint(mouse_pos):
                    return
                
                if btn_export.collidepoint(mouse_pos):
                    filename = f"FAVORITO_{character.get_full_name()}.txt"
                    character.save_to_file(filename)
                    # Feedback visual
                    feedback = pixel_font.render(f"Exportado como {filename}", True, (0, 100, 0))
                    screen.blit(feedback, (WIDTH//2 - feedback.get_width()//2, HEIGHT - 160))
                    pygame.display.flip()
                    pygame.time.delay(1000)  # Mostra o feedback por 1 segundo
                
                if btn_remove.collidepoint(mouse_pos):
                    char_manager.remove_favorite(character)
                    return  # Volta para a lista de favoritos após remover

def main():
    """Função principal que gerencia o fluxo do programa"""
    char_manager = CharacterManager()
    
    while True:
        # Tela inicial com opções
        screen.fill(PARCHMENT)
        
        title = pixel_font_title.render("Gerador de Personagens", True, INK_BROWN)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
        
        btn_generate = draw_button(screen, WIDTH//2 - 150, 200, 300, 50, BUTTON_AGED, "Gerar Personagens")
        btn_favorites = draw_button(screen, WIDTH//2 - 150, 270, 300, 50, BUTTON_AGED, "Ver Favoritos")
        btn_exit = draw_button(screen, WIDTH//2 - 150, 340, 300, 50, BUTTON_AGED, "Sair")
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if btn_generate.collidepoint(mouse_pos):
                    num_characters, should_exit = number_selection_screen()
                    if should_exit:  # Se clicou em Voltar
                        continue  # Volta para o menu principal
                    if num_characters is not None:  # Se selecionou um número
                        character_generation_screen(num_characters, char_manager)
                
                elif btn_favorites.collidepoint(mouse_pos):
                    favorites_screen(char_manager)
                
                elif btn_exit.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                    
if __name__ == "__main__":
    main()
