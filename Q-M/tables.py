


import math


class QuineMcCluskey:

    __version__ = "0.2"



    def __init__(self, use_xor = False):

        self.use_xor = use_xor
        self.n_bits = 0



    def __num2str(self, i):

        x = ['1' if i & (1 << k) else '0' for k in range(self.n_bits - 1, -1, -1)]
        return "".join(x)



    def simplify(self, ones, dc = [], num_bits = None):

        terms = ones + dc
        if len(terms) == 0:
            return None

        if num_bits is not None:
            self.n_bits = num_bits
        else:
            self.n_bits = int(math.ceil(math.log(max(terms) + 1, 2)))

        ones = set(self.__num2str(i) for i in ones)
        dc = set(self.__num2str(i) for i in dc)

        return self.simplify_los(ones, dc)



    def simplify_los(self, ones, dc = [], num_bits = None):

        self.profile_cmp = 0
        self.profile_xor = 0
        self.profile_xnor = 0

        terms = ones | dc
        if len(terms) == 0:
            return None

        if num_bits is not None:
            self.n_bits = num_bits
        else:
            self.n_bits = max(len(i) for i in terms)
            if self.n_bits != min(len(i) for i in terms):
                return None

        prime_implicants = self.__get_prime_implicants(terms)

        essential_implicants = self.__get_essential_implicants(prime_implicants, set(dc))

        return essential_implicants



    def __reduce_simple_xor_terms(self, t1, t2):

        difft10 = 0
        difft20 = 0
        ret = []
        for (t1c, t2c) in zip(t1, t2):
            if t1c == '^' or t2c == '^' or t1c == '~' or t2c == '~':
                return None
            elif t1c != t2c:
                ret.append('^')
                if t2c == '0':
                    difft10 += 1
                else:
                    difft20 += 1
            else:
                ret.append(t1c)
        if difft10 == 1 and difft20 == 1:
            return "".join(ret)
        return None



    def __reduce_simple_xnor_terms(self, t1, t2):

        difft10 = 0
        difft20 = 0
        ret = []
        for (t1c, t2c) in zip(t1, t2):
            if t1c == '^' or t2c == '^' or t1c == '~' or t2c == '~':
                return None
            elif t1c != t2c:
                ret.append('~')
                if t1c == '0':
                    difft10 += 1
                else:
                    difft20 += 1
            else:
                ret.append(t1c)
        if (difft10 == 2 and difft20 == 0) or (difft10 == 0 and difft20 == 2):
            return "".join(ret)
        return None



    def __get_prime_implicants(self, terms):

        n_groups = self.n_bits + 1
        marked = set()


        groups = [set() for i in range(n_groups)]
        for t in terms:
            n_bits = t.count('1')
            groups[n_bits].add(t)
        if self.use_xor:

            for gi, group in enumerate(groups):
                for t1 in group:
                    for t2 in group:
                        t12 = self.__reduce_simple_xor_terms(t1, t2)
                        if t12 != None:
                            terms.add(t12)
                    if gi < n_groups - 2:
                        for t2 in groups[gi + 2]:
                            t12 = self.__reduce_simple_xnor_terms(t1, t2)
                            if t12 != None:
                                terms.add(t12)

        done = False
        while not done:

            groups = dict()
            for t in terms:
                n_ones = t.count('1')
                n_xor  = t.count('^')
                n_xnor = t.count('~')

                assert n_xor == 0 or n_xnor == 0

                key = (n_ones, n_xor, n_xnor)
                if key not in groups:
                    groups[key] = set()
                groups[key].add(t)

            terms = set()
            used = set()

            for key in groups:
                key_next = (key[0]+1, key[1], key[2])
                if key_next in groups:
                    group_next = groups[key_next]
                    for t1 in groups[key]:

                        for i, c1 in enumerate(t1):
                            if c1 == '0':
                                self.profile_cmp += 1
                                t2 = t1[:i] + '1' + t1[i+1:]
                                if t2 in group_next:
                                    t12 = t1[:i] + '-' + t1[i+1:]
                                    used.add(t1)
                                    used.add(t2)
                                    terms.add(t12)


            for key in [k for k in groups if k[1] > 0]:
                key_complement = (key[0] + 1, key[2], key[1])
                if key_complement in groups:
                    for t1 in groups[key]:
                        t1_complement = t1.replace('^', '~')
                        for i, c1 in enumerate(t1):
                            if c1 == '0':
                                self.profile_xor += 1
                                t2 = t1_complement[:i] + '1' + t1_complement[i+1:]
                                if t2 in groups[key_complement]:
                                    t12 = t1[:i] + '^' + t1[i+1:]
                                    used.add(t1)
                                    terms.add(t12)

            for key in [k for k in groups if k[2] > 0]:
                key_complement = (key[0] + 1, key[2], key[1])
                if key_complement in groups:
                    for t1 in groups[key]:
                        t1_complement = t1.replace('~', '^')
                        for i, c1 in enumerate(t1):
                            if c1 == '0':
                                self.profile_xnor += 1
                                t2 = t1_complement[:i] + '1' + t1_complement[i+1:]
                                if t2 in groups[key_complement]:
                                    t12 = t1[:i] + '~' + t1[i+1:]
                                    used.add(t1)
                                    terms.add(t12)

            for g in list(groups.values()):
                marked |= g - used

            if len(used) == 0:
                done = True

        pi = marked
        for g in list(groups.values()):
            pi |= g
        return pi



    def __get_essential_implicants(self, terms, dc):

        perms = {}
        for t in terms:
            perms[t] = set(p for p in self.permutations(t) if p not in dc)


        ei_range = set()
        ei = set()
        groups = dict()
        for t in terms:
            n = self.__get_term_rank(t, len(perms[t]))
            if n not in groups:
                groups[n] = set()
            groups[n].add(t)
        for t in sorted(list(groups.keys()), reverse=True):
            for g in groups[t]:
                if not perms[g] <= ei_range:
                    ei.add(g)
                    ei_range |= perms[g]
        if len(ei) == 0:
            ei = set(['-' * self.n_bits])
        return ei



    def __get_term_rank(self, term, term_range):

        n = 0
        for t in term:
            if t == "-":
                n += 8
            elif t == "^":
                n += 4
            elif t == "~":
                n += 2
            elif t == "1":
                n += 1
        return 4*term_range + n



    def permutations(self, value = ''):


        n_bits = len(value)
        n_xor = value.count('^') + value.count('~')
        xor_value = 0
        seen_xors = 0
        res = ['0' for i in range(n_bits)]
        i = 0
        direction = +1
        while i >= 0:

            if value[i] == '0' or value[i] == '1':
                res[i] = value[i]

            elif value[i] == '-':
                if direction == +1:
                    res[i] = '0'
                elif res[i] == '0':
                    res[i] = '1'
                    direction = +1

            elif value[i] == '^':
                seen_xors = seen_xors + direction
                if direction == +1:
                    if seen_xors == n_xor and xor_value == 0:
                        res[i] = '1'
                    else:
                        res[i] = '0'
                else:
                    if res[i] == '0' and seen_xors < n_xor - 1:
                        res[i] = '1'
                        direction = +1
                        seen_xors = seen_xors + 1
                if res[i] == '1':
                    xor_value = xor_value ^ 1

            elif value[i] == '~':
                seen_xors = seen_xors + direction
                if direction == +1:
                    if seen_xors == n_xor and xor_value == 1:
                        res[i] = '1'
                    else:
                        res[i] = '0'
                else:
                    if res[i] == '0' and seen_xors < n_xor - 1:
                        res[i] = '1'
                        direction = +1
                        seen_xors = seen_xors + 1
                if res[i] == '1':
                    xor_value = xor_value ^ 1

            else:
                res[i] = '#'

            i = i + direction
            if i == n_bits:
                direction = -1
                i = n_bits - 1
                yield "".join(res)


qm = QuineMcCluskey()
ones = [0,1,2,8,9,15,17,21,24,25,27,31]
dontcares = []
print(qm.simplify(ones, dontcares))