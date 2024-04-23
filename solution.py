class solution:

    def __init__(self):
        pass

    def pallindrome_check(self,s:str) -> bool :
        return s == s[::-1]
    
    def inserter(self,lis: list, index: int, item) -> None :
        lis.insert(index,item)
    
    def diff_show(self,a:list, b:list) -> None:
        print(f'Before insert(): {a}')
        a.insert(len(a)//2,'middle')
        print(f'After insert({len(a)//2},\'middle\'): {a}')
        print()
        print(f'Brfore append(): {a}')
        a.append('end')
        print(f'After append(\'end\'): {a}')
        print()
        print(f'Before extend() first list: {a} and second list: {b}')
        a.extend(b)
        print(f'After extend(): {a}')
    
    def counter(self,lis:list) -> dict:
        #There is a mistake in question wording, because
        #number of occurences of each unique elements is always 1 :).
        occurences = {}
        for i in lis:
            if i not in occurences:
                occurences[i] = 0
            occurences[i] += 1
        return occurences
    
    def remove_dup(self,lis:list) -> list:
        #we can also do it by simply set(lis),
        #but the order of elements will be lost.
        ref = []
        for i in lis:
            if i not in ref:
                ref.append(i)
        return ref
    
    def primes(self,n:int) -> list:
        #Efficient algorithm that we've used in math also
        #Algorithm called Sieve of Eratosthenes.
        #Also I think prime numbers start from 2.
        number_list = [True for i in range(n)]
        number = 2
        while number*number <= n:
            for i in range(number*number,n,number):
                if number_list[i]:
                    number_list[i] = False
            number += 1
        prime_list = []
        for i in range(1,len(number_list)):
            if number_list[i]:
                prime_list.append(i)
        return prime_list
    
    def last_remover(self,lis:list) -> None:
        lis.pop()
        return
    
    def check_ele(self,lis:list,ele) -> bool:
        #Not sure if the list is sorted or not.
        #Otherwise I would've used Binary search.
        return ele in lis
    
    def max_in_lis(self,lis:list) :
        ele = float('-inf')
        for i in lis:
            ele = i if i >= ele else ele
        return ele
    
    def merge(self,dic1:dict,dic2:dict) -> None:
        """
            We can directly use the function update()
            from the dictionary class. But that dosen't
            cover the repeating elements. The repeating
            elements gets ignored.
        """
        for i in dic2:
            if i in dic1:
                dic1[i] += dic2[i]
            else:
                dic1[i] = dic2[i]
        return
    
    def remove_occur(self,lis:list,ele) -> list:
        return [i for i in lis if i != ele]
    
    def most_expensive(self,prices:dict) -> str:
        maxx = -1 #Because price can never be negative, isn't it?
        item = None
        for i in prices:
            if prices[i] > maxx:
                maxx = prices[i]
                item = i
        return item
    
    def reverse_dict(self,dic:dict) -> dict:
        return {j:i for i,j in dic.items()}
    
    def remove_ele_dict(self,dic:dict,item) -> None:
        for i in dic:
            if dic[i] == item:
                del dic[i]
        return
    
    def tup_add(self,tup1:tuple,tup2:tuple) -> tuple:
        return tup1 + tup2
    
    def average_height(self,heights:tuple) -> float:
        return sum(heights) / len(heights)
    
    def element_finder(self,tup:tuple,ele) -> int:
        return tup.index(ele) if ele in tup else None
    
    def capitalize_each_word(self,sentence:str) -> str:
        return " ".join([i.capitalize() for i in sentence.strip().split()])
    
    def reverse_words_sentence(self,sentence:str) -> str:
        return " ".join([i for i in sentence.strip().split()[::-1]])
    
    def longest_word(self,sentence:str) -> str:
        return sorted(sentence.strip().split(),key=len,reverse=True)[0]



if __name__ == "__main__":
    sol = solution()
    '''
        Can use any function just by calling with object sol
    '''

