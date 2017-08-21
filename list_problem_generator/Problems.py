import numpy as np
import random

class GenList(object):
    def __init__(self, index):
        """
        Args:
            index: True or False, indicates presence or absence of
            index-specific item(s) in the generated list.
        """
        self.index = index
    def gen_length(self):
        """
        Generate a length for the generated list.
        
        Returns:
            int: random int from 0 - 20.
        """
        return np.random.choice(range(0, 21))
    def gen_int(self, lo=0, hi=1000):
        """
        Generate an int for the generated list.
        
        Returns:
            int: random int from 0 - 1000.
        """
        return np.random.choice(range(lo, hi+1))
    def gen_index(self, new_list):
        """
        Generate an index list of length 1 - 5 to be prepended
        or appended to new_list.
        
        Returns:
            list: final generated list with index-specific int(s)
            as the first or last items of the list.
        """
        front_or_back = ["head", "tail"]
        index_list = []
        index_quant = np.random.choice(range(1, 6))
        for index in range(index_quant):
            index_list.append(np.random.choice(range(0, len(new_list))))
        if random.choice(front_or_back) == "head":
            return index_list + new_list
        else:
            return new_list + index_list
        
    def make_list(self):
        """
        Generate a list of length 0 - 20, in which each item is a random int
        from 0 - 1000. Depending on the object's 'index' attribute, the list
        may also contain 1 - 5 index-related items at the beginning or end of 
        the list.
        
        Returns:
            list: final generated list.
        """
        new_list = []
        for i in range(self.gen_length()):
            new_list.append(self.gen_int())
        if self.index:
            return self.gen_index(new_list)
        else:
            return new_list
    
class head(object):
    def __init__(self, eval_amount_list):
        self.eval = eval_amount_list
        self.eval_dict = {}
    def evaluate(self):
        if type(self.eval) == list:
            self.eval_dict[str(self.eval)] = self.eval[0]
        else:
            for current_eval in range(self.eval):
                eval_list = GenList(False).make_list()
                self.eval_dict[str(eval_list)] = eval_list[0]                
    def generate(self):
        self.evaluate()
        return self.eval_dict

class tail(object):
    def __init__(self, eval_amount_list):
        self.eval = eval_amount_list
        self.eval_dict = {}
    def evaluate(self):
        if type(self.eval) == list:
            self.eval_dict[str(self.eval)] = self.eval[1:]
        else:
            for current_eval in range(self.eval):
                eval_list = GenList(False).make_list()
                self.eval_dict[str(eval_list)] = eval_list[1:]                
    def generate(self):
        self.evaluate()
        return self.eval_dict

class reverse(object):
    def __init__(self, eval_amount_list):
        self.eval = eval_amount_list
        self.eval_dict = {}
    def evaluate(self):
        if type(self.eval) == list:
            self.eval_dict[str(self.eval)] = self.eval[::-1] 
        else:
            for current_eval in range(self.eval):
                eval_list = GenList(False).make_list()
                self.eval_dict[str(eval_list)] = eval_list[::-1]              
    def generate(self):
        self.evaluate()
        return self.eval_dict
    
class slt(object):
    def __init__(self, eval_amount_list, slt_what):
        self.eval = eval_amount_list
        self.slt_what = slt_what
        self.eval_dict = {}
    def evaluate(self):
        if type(self.eval) == list:
            if self.slt_what == "random":
                curr_slt_what = np.random.choice(range(0, 1001))
                self.eval_dict[(str(curr_slt_what) + " " + \
                str(self.eval))] = curr_slt_what > sum(self.eval)
            elif self.slt_what == "index_0":
                self.eval_dict[(str(self.eval[0]) + " " + \
                str(self.eval[1:]))] = self.eval[0] > sum(self.eval[1:])
            else:
                self.eval_dict[(str(self.slt_what) + " " + \
                str(self.eval))] = self.slt_what > sum(self.eval)
        else:
            for current_eval in range(self.eval):
                eval_list = GenList(False).make_list()
                if self.slt_what == "random":
                    curr_slt_what = np.random.choice(range(0, 10001))
                    self.eval_dict[(str(curr_slt_what) + " " + \
                    str(eval_list))] = curr_slt_what > sum(eval_list)
                elif self.slt_what == "index_0":
                    self.eval_dict[(str(eval_list[0]) + " " + \
                    str(eval_list[1:]))] = eval_list[0] > sum(eval_list[1:])
                else:
                    self.eval_dict[(str(self.slt_what) + " " + \
                    str(eval_list))] = self.slt_what > sum(eval_list)
    def generate(self):
        self.evaluate()
        return self.eval_dict
        
