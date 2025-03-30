"""  zkusila jsem sama s pomocí existujících souborů, pak jsem konzultovala gpt"""

print(" ")
print("zacatekkkkk_____________________________________________________________________---zacatek________________-")

from dataclasses import dataclass
from typing import Any

@dataclass
class Element:
    hodnota: Any  # Libovolná hodnota uložená v prvku
    priorita: int  # Priorita prvku (čím nižší, tím dříve bude zpracován)

class BinaryHeap:    
    def __init__(self):
        self.halda = []
    
    def push(self, prvek: Element):
        self.halda.append(prvek)
        self._oprav_nahoru(len(self.halda) - 1)

    def pop(self):
        if not self.halda:
            raise Exception("Halda je prázdná")
        if len(self.halda) == 1:
            return self.halda.pop()
        
        min_prvek = self.halda[0]  # Nejmenší prvek (kořen)
        self.halda[0] = self.halda.pop()  # Poslední prvek přesuneme na místo kořene
        self._oprav_dolu(0)  # Oprava haldy směrem dolů
        return min_prvek
    
    def head(self):
        if not self.halda:
            raise Exception("Halda je prázdná")
        return self.halda[0]
    
    def _oprav_nahoru(self, index):
        rodic_index = (index - 1) // 2
        while index > 0 and self.halda[index].priorita < self.halda[rodic_index].priorita:
            self.halda[index], self.halda[rodic_index] = self.halda[rodic_index], self.halda[index]
            index = rodic_index
            rodic_index = (index - 1) // 2
    
    def _oprav_dolu(self, index):
        velikost = len(self.halda)
        while True:
            levy_potomek = 2 * index + 1  # Levý potomek
            pravy_potomek = 2 * index + 2  # Pravý potomek
            nejmensi = index  # Předpokládáme, že rodič je nejmenší
            
            if levy_potomek < velikost and self.halda[levy_potomek].priorita < self.halda[nejmensi].priorita:
                nejmensi = levy_potomek
            
            if pravy_potomek < velikost and self.halda[pravy_potomek].priorita < self.halda[nejmensi].priorita:
                nejmensi = pravy_potomek
            
            if nejmensi == index:
                break  # Halda je správně, končíme
            
            self.halda[index], self.halda[nejmensi] = self.halda[nejmensi], self.halda[index]
            index = nejmensi


from halda_bi import BinaryHeap, Element

def push(heap, priority):
    heap.push(Element(priority, priority))

def test_push() -> None:
    heap = BinaryHeap()
    push(heap, 5)
    assert heap.head().priority == 5
    push(heap, 8)
    assert heap.head().priority == 5
    push(heap, 4)
    assert heap.head().priority == 4
    push(heap, 7)
    assert heap.head().priority == 4
    push(heap, 10)
    assert heap.head().priority == 4
    push(heap, 2)
    assert heap.head().priority == 2

def test_push_pop() -> None:
    heap = BinaryHeap()
    push(heap, 5)
    push(heap, 8)
    push(heap, 4)
    assert heap.pop().priority == 4
    assert heap.head().priority == 5

    # another push round
    push(heap, 7)
    push(heap, 10)
    push(heap, 2)
    assert heap.pop().priority == 2
    assert heap.pop().priority == 5
    assert heap.pop().priority == 7
    assert heap.pop().priority == 8
    assert heap.pop().priority == 10



print(" ")
print("koneccccccccccccccc___________________________________________________________koneccccccccccccc____________________--- ")