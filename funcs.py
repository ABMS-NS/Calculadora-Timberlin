import numpy as np
from decimal import Decimal, ROUND_HALF_UP
import math

class Calculos:

    def vida_base(lvl:int):
        # Cálculo da vida base baseado no nível do personagem
        if lvl <= 5:
            return 15
        elif 6 <= lvl <= 10:  # Simplificado a verificação de intervalo
            return 20
        elif 11 <= lvl <= 25:
            return 25
        elif 26 <= lvl <= 35:
            return 30
        elif 36 <= lvl <= 45:
            return 50
        elif lvl == 46:
            return 95
        elif lvl == 47:
            return 190
        elif lvl == 48:
            return 285
        elif lvl == 49:
            return 380
        elif lvl == 50:
            return 400
        else:
            return 15
        
    def alma_base(lvl:int):
        # Cálculo da alma base baseado no nível do personagem
        if lvl <= 5:
            return 25
        elif 6 <= lvl <= 10:  # Simplificado a verificação de intervalo
            return 45
        elif 11 <= lvl <= 25:
            return 50
        elif 26 <= lvl <= 35:
            return 75
        elif 36 <= lvl <= 45:
            return 100
        elif 46 <= lvl < 50:
            return 125
        elif lvl == 50:
            return 150
        else:
            return 25
        
    def vigorpor2(vigor:int):
        # Retorna o vigor dividido por 2, com valor mínimo de 1
        if vigor < 2:
            return 1
        else:
            return vigor / 2
        
    def vigormenos2(vigor:int):
        # Retorna o vigor menos 2, com valor mínimo de 1
        if vigor <= 2:
            return 1
        else:
            return vigor - 2
    
    def vigormenos1(vigor:int):
        # Retorna o vigor menos 1, com valor mínimo de 1
        if vigor <= 1:
            return 1
        else:
            return vigor - 1
        
    def arredondar(valor):
        # Arredonda o valor usando o método de arredondamento bancário
        return int(Decimal(valor).quantize(0, rounding=ROUND_HALF_UP))
        
class Check: # Funções de verificação para classes, origens e trilhas

    # Classes (bauticabauau)
    def desafiante(classe):
        # Verifica se a classe é Desafiante
        if classe == "Desafiante":
            return True
        else:
            return False
    
    def bastiao(classe):
        # Verifica se a classe é Bastião
        if classe == "Bastião":
            return True
        else:
            return False
    
    def equilibrista(classe):
        # Verifica se a classe é Equilibrista
        if classe == "Equilibrista":
            return True
        else:
            return False   
    
    def socorrista(classe):
        # Verifica se a classe é Socorrista
        if classe == "Socorrista":
            return True
        else:
            return False
    
    def atirador(classe):
        # Verifica se a classe é Atirador
        if classe == "Atirador":
            return True
        else:
            return False
        
    def amaldiçoado(classe):
        # Verifica se a classe é Amaldiçoado
        if classe == "Amaldiçoado":
            return True
        else:
            return False

    # Origens (bauticabauau)
    def manipulador(origem):
        # Verifica se a origem é Manipulador
        if origem == "Manipulador de alma":
            return True
        else:
            return False
        
    def retornado(origem):
        # Verifica se a origem é Retornado
        if origem == "Retornado":
            return True
        else:
            return False
        
    def espirituoso(origem):
        # Verifica se a origem é Espirituoso
        if origem == "Espirituoso":
            return True
        else:
            return False
    
    def artista_astral(origem):
        # Verifica se a origem é Artista Astral
        if origem == "Artista Astral":
            return True
        else:
            return False
    

    #buffs 

    def artista_buff(buff_origem):
        # Verifica se tem buff de Artista
        if buff_origem == "Artista Astral":
            return True
        else:
            return False
        
    def sub_artista_espirito(suborigem):
        # Verifica se a suborigem é relacionada a artista ou espírito
        if suborigem == "Artista Astral" or suborigem == "Espirituoso":
            return True
        else:
            return False
    
        
    # Sub classes (bauticabauau)
    def algoz(subclasse):
        # Verifica se a subclasse é Algoz
        if subclasse == "Algoz":
            return True
        else:
            return False
    
    def berserk(subclasse):
        # Verifica se a subclasse é Berserk
        if subclasse == "Berserk":
            return True
        else:
            return False
    
    def duelista(subclasse):
        # Verifica se a subclasse é Duelista
        if subclasse == "Duelista":
            return True
        else:
            return False
        
    def inabalavel(subclasse):
        # Verifica se a subclasse é Inabalável
        if subclasse == "Inabalável":
            return True
        else:
            return False
    
    def etereo(subclasse):
        # Verifica se a subclasse é Etéreo
        if subclasse == "Etéreo":
            return True
        else:
            return False
        
    def artesao(subclasse):
        # Verifica se a subclasse é Artesão
        if subclasse == "Artesão":
            return True
        else:
            return False
    
    def xama(subclasse):
        # Verifica se a subclasse é Xamã
        if subclasse == "Xamã":
            return True
        else:
            return False
        
class Alma:

    def calcular(lvl: int, origem: int, alma: int, bonus: int):
        # Cálculo dos pontos de alma baseado no nível, origem e atributo de alma

        # 25 + Alma Base + ( Alma * 3 ) + Bônus de Classe ou Raça
        if Check.manipulador(origem):  # Simplificado a verificação booleana
            return 25 + Calculos.alma_base(lvl) + (alma * 3) + bonus + (alma * 5)
        elif Check.retornado(origem):
            return 25 + Calculos.alma_base(lvl) + (alma * 3) + bonus + (alma * 4)
        else: 
            return 25 + Calculos.alma_base(lvl) + (alma * 3) + bonus

class Vida:

    def calcular(lvl: int, classe: int, subclasse: int, vigor: int, firmeza: int, bonus: int):
        # Cálculo dos pontos de vida baseado na classe, subclasse e atributos

        if Check.desafiante(classe):
            if Check.berserk(subclasse):
                return Calculos.arredondar(Calculos.vida_base(lvl) + (vigor * lvl) + (lvl * vigor) + 5 + bonus) # VidaBase+(VIG * LV) + (LV * VIG ) + 5
            elif Check.algoz(subclasse):
                return Calculos.vida_base(lvl) + (vigor * lvl) + lvl + bonus
            else:
                return Calculos.arredondar(Calculos.vida_base(lvl) + (vigor * lvl) + (lvl * (Calculos.vigorpor2(vigor))) + bonus)
            
        elif Check.bastiao(classe):
            if Check.inabalavel(subclasse):
                return Calculos.vida_base(lvl) + (vigor * lvl) + (vigor * firmeza) + (lvl * 2) + bonus # Vida Base +(VIG * LV) + ( VIG * BonusDeFirmeza) + ( LV * 2 )
            else:
                return Calculos.vida_base(lvl) + (vigor * lvl) + (vigor * firmeza) + lvl + bonus # Vida Base +(VIG * LV) + ( VIG * BonusDeFirmeza) + LV
            
        elif Check.equilibrista(classe):
                return Calculos.vida_base(lvl) + ((Calculos.vigormenos1(vigor)) * lvl) + lvl + bonus
        
        elif Check.socorrista(classe):
                return Calculos.vida_base(lvl) + ((Calculos.vigormenos1(vigor)) * lvl) + lvl + bonus
        
        elif Check.atirador(classe):
                return Calculos.vida_base(lvl) + ((Calculos.vigormenos2(vigor)) * lvl) + lvl + bonus
        
        elif Check.amaldiçoado(classe):
            if Check.etereo(subclasse):
                return Calculos.arredondar(Calculos.vida_base(lvl) + (vigor * lvl) + (lvl * (Calculos.vigorpor2(vigor))) + bonus) # VidaBase+(VIG * LV) + (LV * ( Vig/2) ) + Bonus de Classe 
            else:
                return Calculos.vida_base(lvl) + ((Calculos.vigormenos2(vigor)) * lvl) + lvl + bonus

class Estamina:

    def calcular(lvl: int, classe: int, subclasse: int, vigor: int, firmeza: int, medicina:int, bonus: int):
        # Cálculo dos pontos de estamina baseado na classe, subclasse e atributos

        if Check.desafiante(classe):
            if Check.duelista(subclasse):
                return 30 + (((vigor*2) + firmeza) * 3) + bonus # 30 + ( ( ( VIG*2) +Firmeza) * 3 )
            else: 
                return Calculos.arredondar(25 + ((vigor + firmeza) * 3) + 9 + bonus) # 25 + ( (VIG+Firmeza) * 3 ) + 9
            
        elif Check.bastiao(classe):  
            return 20 + ((vigor + firmeza) * 2) + bonus # 20 + ( (VIG+Firmeza) * 2 ) + Bônus de Classe ou Raça
        
        elif Check.equilibrista(classe):
            if Check.artesao(subclasse):
                return 50 + ((Calculos.vigormenos1(vigor) + firmeza) * 2) + bonus
            else: 
                return 20 + ((Calculos.vigormenos1(vigor) + firmeza) * 2) + bonus  # Corrigido: adicionado 'return'

        elif Check.socorrista(classe):
            return 20 + ((Calculos.vigormenos1(vigor) + firmeza) * 2) + (medicina * 2) # 20 + ( ( VIG+Firmeza ) * 2 ) + ( Medicina * 2 )
        
        elif Check.atirador(classe):
            return 25 + ((vigor+firmeza) * 2) + ((vigor * 2) + 1) # 25 + ( ( VIG+Firmeza ) * 2 ) + (( VIG * 2) + 1)
        
        elif Check.amaldiçoado(classe):
            return 20 + ((vigor + firmeza) * 2) + bonus
        
        else:
            return 20 + ((vigor + firmeza) * 2) + bonus
        
class Espirito:

    def calcular(lvl: int, classe: int, subclasse: int, origem: int, suborigem: int, buff_origem: int, alma: int, espiritualidade: int, bonus: int,):
        # Cálculo dos pontos de espírito baseado na classe, subclasse, origem e atributos
        const_1 = 1
        const_2 = 2
        const_3 = 3
        const_4 = 4
        const_5 = 5
        const_6 = 6
        const_7 = 7

        # Se for artista ou espirituoso aumenta mais 1 nos multiplicadores
        if Check.artista_astral(origem) or Check.espirituoso(origem):  # Simplificado a verificação booleana
            const_1 += 1
            const_2 += 1
            const_3 += 1
            const_4 += 1
            const_5 += 1
            const_6 += 1
            const_7 += 1

            # Se tiver buff de artista astral, soma +1
            if Check.artista_buff(buff_origem):
                const_1 += 1
                const_2 += 1
                const_3 += 1
                const_4 += 1
                const_5 += 1
                const_6 += 1
                const_7 += 1
        
        # Se tiver suborigem de artista ou espirituoso, soma +0.5
        if Check.sub_artista_espirito(suborigem):
            const_1 += 0.5
            const_2 += 0.5
            const_3 += 0.5
            const_4 += 0.5
            const_5 += 0.5
            const_6 += 0.5
            const_7 += 0.5

        if Check.desafiante(classe):
            return Calculos.arredondar((lvl * const_3) + (5+(alma * const_3)) + espiritualidade + bonus) # ( Lv * 3) + (5+ (ALM * 3) + Espiritualidade
        
        elif Check.bastiao(classe):
            return Calculos.arredondar((lvl * const_3) + (5+(alma * const_3)) + espiritualidade + bonus) 
        
        elif Check.equilibrista(classe):
            return Calculos.arredondar((lvl * const_4) + (7 + (alma * const_4) + (espiritualidade * const_3) + bonus))  # ( Lv * 4 ) + ( 7+ (ALM * 4 ) + ( Espiritualidade * 3 )
        
        elif Check.socorrista(classe):
            return Calculos.arredondar((lvl * const_3) + (5+(alma * const_3)) + espiritualidade + bonus)
        
        elif Check.atirador(classe):
            return Calculos.arredondar((lvl * const_3) + (5+(alma * const_3)) + espiritualidade + bonus)
        
        elif Check.amaldiçoado(classe):
            if Check.xama(subclasse):
                return Calculos.arredondar((lvl * const_5) + (10 + (alma * const_5)) + (espiritualidade * const_5) + bonus) # ( Lv * 5 ) + ( 10 + ( ALM * 5 ) + ( Espiritualidade * 5 )
            else:
                return Calculos.arredondar((lvl * const_4) + (10 + (alma * const_5)) + (espiritualidade * const_4) + bonus) # ( Lv * 4 ) + ( 10 + (ALM * 5 ) + ( Espiritualidade * 4 )
        
        else:  # Adicionado para lidar com outros casos não especificados
            return Calculos.arredondar((lvl * const_3) + (5+(alma * const_3)) + espiritualidade + bonus)