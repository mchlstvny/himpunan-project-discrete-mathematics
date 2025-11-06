class Himpunan:
    def __init__(self, *args):
        self.data = []
        for item in args:
            if isinstance(item, (list, set, tuple)):
                for i in item:
                    if i not in self.data:
                        self.data.append(i)
            else:
                if item not in self.data:
                    self.data.append(item)

    def __repr__(self):
        return "{" + ", ".join(map(str, self.data)) + "}"

    # Tambah anggota
    def __iadd__(self, item):
        if item not in self.data:
            self.data.append(item)
        return self

    # Hapus anggota
    def __isub__(self, item):
        if item in self.data:
            self.data.remove(item)
        return self

    # Panjang himpunan
    def __len__(self):
        return len(self.data)

    # Cek apakah item ada dalam himpunan
    def __contains__(self, item):
        return item in self.data

    # Cek kesetaraan
    def __eq__(self, other):
        return sorted(self.data) == sorted(other.data)

    # Subset, proper subset, dan superset
    def __le__(self, other):
        return all(item in other.data for item in self.data)

    def __lt__(self, other):
        return self <= other and self != other

    def __ge__(self, other):
        return all(item in self.data for item in other.data)

    # Ekuivalen (elemen sama, urutan bebas)
    def __floordiv__(self, other):
        return set(self.data) == set(other.data)

    # Gabungan (A ∪ B)
    def __add__(self, other):
        result = list(self.data)
        for x in other.data:
            if x not in result:
                result.append(x)
        return Himpunan(*result)

    # Irisan (A ∩ B)
    def __truediv__(self, other):
        result = [x for x in self.data if x in other.data]
        return Himpunan(*result)

    # Selisih (A - B)
    def __sub__(self, other):
        result = [x for x in self.data if x not in other.data]
        return Himpunan(*result)

    # Selisih Simetris (A ⊕ B)
    def __mul__(self, other):
        result = [x for x in self.data if x not in other.data] + \
                 [x for x in other.data if x not in self.data]
        return Himpunan(*result)

    # Perkalian Kartesius (A × B)
    def __pow__(self, other):
        result = [(a, b) for a in self.data for b in other.data]
        return result

    # Himpunan Kuasa
    def ListKuasa(self):
        hasil = [[]]
        for elemen in self.data:
            hasil += [subset + [elemen] for subset in hasil]
        return [Himpunan(*subset) for subset in hasil]