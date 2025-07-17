import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 850, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gerador de Personagens")

# Cores
GAINSBORO = (220, 220, 220) # cinza claro
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (138, 43, 130)  # blue violeta

# Fontes
font = pygame.font.SysFont('Arial', 16)
title_font = pygame.font.SysFont('Arial', 24, bold=True)

# Listas de nomes masculinos
male_names = [
    # Portugueses/Brasileiros
    "João", "Pedro", "Carlos", "Miguel", "Rafael", "Antônio", "Fernando", 
    "Ricardo", "Gustavo", "Eduardo", "Marcos", "Lucas", "Daniel", "Paulo",
    # Ingleses
    "John", "James", "Robert", "Michael", "William", "David", "Joseph", 
    "Daniel", "Matthew", "Christopher", "Andrew", "Edward",
    # Alemães
    "Hans", "Klaus", "Wolfgang", "Dieter", "Friedrich", "Heinrich", "Johann",
    "Karl", "Stefan", "Thomas", "Ulrich", "Werner"
]

# Listas de nomes femininos
female_names = [
    # Portugueses/Brasileiros
    "Maria", "Ana", "Lucia", "Sofia", "Isabella", "Laura", "Beatriz", 
    "Camila", "Amanda", "Juliana", "Carolina", "Patrícia", "Fernanda", "Raquel",
    # Ingleses
    "Mary", "Emma", "Olivia", "Sophia", "Ava", "Mia", "Charlotte", "Amelia",
    "Elizabeth", "Margaret", "Emily", "Victoria",
    # Alemães
    "Greta", "Ingrid", "Helga", "Ursula", "Elsa", "Marta", "Anneliese",
    "Clara", "Hannah", "Lena", "Sophie", "Anna"
]

noble_surnames = ["Adnor", "Frokz", "Stentyrm", "Vrikz", "Elslinir", "Rotavsk", "Cronas", "Brunks", "Sylens"]
common_surnames = ["Rosters", "Bonglers", "Mklaver", "Drawnd", "Foilty"]
dark_surnames = ["Blonkis", "Grwannir", "Duwnm", "Honsto", "Gwalner", "Vrowntan", "Delins"]

# Detalhes únicos
unique_details = [
    "Sempre está cheirando a cigarro",
    "Anda com um crucifixo que tem um guarda-fotos dentro",
    "Está sempre comendo doces",
    "Sempre escrevendo algo em um caderno ou lendo",
    "Tem o hábito de tamborilar os dedos quando pensa",
    "Sempre arruma os óculos a cada 5 minutos",
    "Tem um lenço bordado que nunca usa, só fica olhando",
    "Canta baixinho quando está concentrado",
    "Tem um relógio de bolso que nunca funciona",
    "Sempre traz um guarda-chuva, mesmo em dias ensolarados",
    "Tem o hábito de contar moedas no bolso",
    "Sempre chega 10 minutos antes de qualquer compromisso",
    "Tem um anel que gira compulsivamente no dedo",
    "Sempre traz consigo um pequeno saco de ervas aromáticas",
    "Tem o hábito de arrancar etiquetas de roupas novas",
    "Sempre usa meias de cores diferentes",
    "Tem um pequeno caderno de endereços cheio de anotações",
    "Sempre traz um pequeno travesseiro para onde vai",
    "Tem uma cicatriz no queixo que coça quando está nervoso",
    "Sempre traz um pequeno animal de pelúcia na mochila",
    "Tem o hábito de rabiscar margens de livros e papéis",
    "Sempre usa um chapéu, mesmo dentro de casa",
    "Tem uma coleção de botões na bolsa",
    "Sempre traz consigo um pequeno espelho de bolso",
    "Tem o hábito de morder a ponta da caneta quando pensa"
]

class Character:
    def __init__(self):
        self.generate()
    
    def generate(self):
        # Gênero (apenas Masculino ou Feminino)
        self.gender = random.choice(["Masculino", "Feminino"])
        
        # Gera nome conforme o gênero
        if self.gender == "Masculino":
            self.first_name = random.choice(male_names)
        else:
            self.first_name = random.choice(female_names)
        
        # Raças/Seres
        self.race = random.choice([
            "Humano", "Demônio", "Anjo", "Feiticeiro", 
            "Cientista", "Vazio"
        ])
        
        # Características físicas básicas
        self.hair_color = random.choice([
            "Preto", "Castanho", "Loiro", "Ruivo", 
            "Cinza", "Branco", "Colorido"
        ])
        self.eye_color = random.choice([
            "Azul", "Verde", "Castanho", "Preto", 
            "Cinza", "Vermelho", "Âmbar"
        ])
        self.height = random.randint(150, 200)
        
        # Cicatriz da raça
        self.scar = self.generate_scar()
        
        # Classe/Profissão
        self.profession = random.choice([
            "Ladrão", "Assassino", "Agente", "Trabalhador", 
            "Viajante", "Comerciante", "Empresário", "Jornalista",
            "Enfermeiro", "Curandeiro", "Rico", "Químico", 
            "Criacionista", "Ocultista"
        ])
        
        # Personalidade
        self.personality = random.choice([
            "Bravo", "Alegre", "Sério", "Tímido", "Extrovertido", 
            "Sábio", "Ingênuo", "Cínico", "Leal", "Trapaceiro",
            "Misterioso", "Melancólico", "Entusiasta", "Calculista"
        ])
        
        # História/Origem
        self.background = random.choice([
            "Celestial", "Nobre", "Rico", "Centro", 
            "Interior Rural", "Florestal", "Fendas", "Nulo"
        ])
        
        # Gera sobrenome baseado na origem
        if self.background in ["Celestial", "Nobre", "Rico"]:
            self.surname = random.choice(noble_surnames)
        elif self.background in ["Fendas", "Nulo"]:
            self.surname = random.choice(dark_surnames)
        else:
            self.surname = random.choice(common_surnames)
        
        # Detalhe único
        self.unique_detail = random.choice(unique_details)
    
    def generate_scar(self):
        # Cicatriz que identifica a raça
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
        return f"{self.first_name} {self.surname}"

def draw_character(screen, character):
    # Fundo
    screen.fill(LIGHT_BLUE)
    
    # Título
    title = title_font.render("Gerador de Personagem", True, BLACK)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 15))
    
    # Nome completo
    name = title_font.render(character.get_full_name(), True, BLACK)
    screen.blit(name, (WIDTH//2 - name.get_width()//2, 45))
    
    # Botão de gerar novo
    pygame.draw.rect(screen, GRAY, (WIDTH//2 - 100, HEIGHT - 60, 200, 40), border_radius=5)
    btn_text = font.render("Gerar Novo", True, BLACK)
    screen.blit(btn_text, (WIDTH//2 - btn_text.get_width()//2, HEIGHT - 50))
    
    # Informações do personagem
    y_offset = 90
    
    # Desenha um retângulo para as informações
    info_rect = pygame.Rect(50, 80, WIDTH - 100, HEIGHT - 160)
    pygame.draw.rect(screen, GAINSBORO, info_rect, border_radius=10)
    pygame.draw.rect(screen, BLACK, info_rect, 2, border_radius=10)
    
    # Características básicas
    basic_info = [
        f"Raça: {character.race}",
        f"Gênero: {character.gender}",
        f"Altura: {character.height}cm",
        f"Cabelo: {character.hair_color}",
        f"Olhos: {character.eye_color}",
        f"Cicatriz: {character.scar}"
    ]
    
    for info in basic_info:
        text = font.render(info, True, BLACK)
        screen.blit(text, (70, y_offset))
        y_offset += 25
    
    y_offset += 10
    
    # Classe e personalidade
    other_info = [
        f"Classe: {character.profession}",
        f"Personalidade: {character.personality}",
        f"Origem: {character.background}",
        f"Detalhe único: {character.unique_detail}"
    ]
    
    for info in other_info:
        text = font.render(info, True, BLACK)
        screen.blit(text, (70, y_offset))
        y_offset += 25

def main():
    clock = pygame.time.Clock()
    character = Character()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se clicou no botão
                mouse_pos = pygame.mouse.get_pos()
                if WIDTH//2 - 100 <= mouse_pos[0] <= WIDTH//2 + 100 and HEIGHT - 60 <= mouse_pos[1] <= HEIGHT - 20:
                    character.generate()
        
        draw_character(screen, character)
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
