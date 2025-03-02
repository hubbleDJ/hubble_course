"""Home work 2025_02_26"""
# Создать любой класс с минимум тремя свойствами и тремя методами
# Создать новый класс на основе предыдущего
# Добавить в новый класс несколько новых методов и свойств

# Придумать идею для своего бота. Если он будет решать какую-то вашу проблему - будет еще лучше
# Зарегистрировать бота в @BotFather в телеграм

from uuid import uuid1
from time import time  

class Sessions:
    """Здесь записываются данные сессии"""

    def __init__(
        self,
        clients_phrases: list[str],
        bots_phrases: list[str],
        intents: list[str],
        accuracy: list[float]
    ) -> None: 
        
        self.clients_phrases = clients_phrases
        self.bots_phrases = bots_phrases
        self.intents = intents
        self.accuracy = accuracy

    def created_session(self) -> None:
        """Создание сессии"""

        if hasattr(self, 'id'):
            pass
        else:
            self.id = str(uuid1()) 
            self.time = str(time())
    
    def add_new_phrase(
        self,
        clients_phrase: str,
        bots_phrase: str,
        intent: str,
        accuracy: float
        ) -> None:
        """Добавление новых реплик в сессию"""

        self.clients_phrases.append(clients_phrase)
        self.bots_phrases.append(bots_phrase)
        self.intents.append(intent)
        self.accuracy.append(accuracy)

    def delete_phrase(
        self,
        index: int 
    ) -> None:
        """Удаляем реплики из сесси по индексу"""

        if index <= len(self.clients_phrases) and index >= 0:
            self.clients_phrases.pop(index)
            self.bots_phrases.pop(index)
            self.intents.pop(index)
            self.accuracy.pop(index)
        else:
            print(f"Вы вы ввели неправильный индекс. В сесси всего реплик {len(self.clients_phrases)}")

session1: Sessions = Sessions(["Маму в кино водил"], ["Чью?"], ["negative"], [0.99])
Sessions.created_session(session1)
session1.add_new_phrase("Че?", "Извините я вас не понял", "other", 0.78)

print(f'{session1.clients_phrases} {session1.bots_phrases} {session1.id} {session1.accuracy} {session1.time}')

session1.delete_phrase(2.5)
print(f'{session1.clients_phrases} {session1.bots_phrases} {session1.id} {session1.accuracy} {session1.time}')


class AdvancedSession(Sessions):
    """Более расширенная информация о сессии, сбор статистики"""

    def __init__(
        self, 
        clients_phrases: list[str], 
        bots_phrases: list[str], 
        intents: list[str], 
        accuracy: list[float], 
        clients_id: str)-> None:
        super().__init__(clients_phrases, bots_phrases, intents, accuracy)
        self.clients_id = clients_id

    def get_statistic(self) -> dict:
        """возвращает сколько было интентов и какие, а также среднюю точность по боту"""
        return {
            "Сколько интентов было: ": len(self.intents),
            "Какие интенты: ": self.intents,
            "Средняя точность ": sum(self.accuracy) / len(self.accuracy) if self.accuracy else 0
        }

session3: AdvancedSession = AdvancedSession(
    ["Привет"],
    ["Привет"],
    ["greeting"],
    [1.0],
    '01',
)

print(session3.get_statistic())