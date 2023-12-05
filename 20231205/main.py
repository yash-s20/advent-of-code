
class DefaultKeyDict:
    def __init__(self):
        self.src_starts = []
        self.dst_starts = []
        self.ranges = []
    
    def set_many(self, dst, src, r):
        self.ranges.append(r)
        self.dst_starts.append(dst)
        self.src_starts.append(src)
    def sort(self):
        sdr = sorted(zip(self.src_starts, self.dst_starts, self.ranges))
        self.src_starts, self.dst_starts, self.ranges = zip(*sdr)
    
    def get_many(self, src, r):
        # print(src, r)
        for ss, ds, rs in zip(self.src_starts, self.dst_starts, self.ranges):
            if r == 0:
                return
            if ss + rs < src:
                continue
            if ss >= src + r:
                continue
            cover = ss - src
            if cover > 0:
                yield (src, min(r, cover))
                src += min(r, cover)
                r -= min(r, cover)
                if r == 0:
                    return
            far_in = src - ss
            max_in = min(ss + rs, src + r)
            yield (ds + far_in, max_in - src)
            r -= (max_in - src)
            src = max_in
        if r > 0:
            yield (src, r)

    def __getitem__(self, key):
        for (s, d, r) in zip(self.src_starts, self.dst_starts, self.ranges):
            if s <= key < s + r:
                return d + key - s
        return key

    def __setitem__(self, key, value):
        self.ranges.append(1)
        self.dst_starts.append(value)
        self.src_starts.append(key)


    def __str__(self):
        return f"srcs: {self.src_starts}, dsts: {self.dst_starts}, ranges: {self.ranges}"

def apply_all_maps(maps, keys):
    for k in keys:
        for m in maps:
            k = m[k]
        yield k

def aam(maps, keys):
    for i, m in enumerate(maps):
        # print(i, m)
        new_keys = []
        for (src, ran) in keys:
            new_keys += list(m.get_many(src, ran))
            print(new_keys)
        keys = new_keys
    starts = [s for (s, _) in keys]
    return starts

if __name__ == "__main__":
    lines = open('input.txt', 'r')
    mappings = []
    mapping = None
    for line in lines:
        line = line.strip()
        if "seeds" in line:
            _, seeds = line.split(':')
            seeds = seeds.strip().split()
            seeds = [int(s) for s in seeds]
            final_seeds = []
            num_ranges = len(seeds) // 2
            final_seeds = [(seeds[2 * i], seeds[2 * i + 1]) for i in range(num_ranges)]
            # for i in range(num_ranges):
                # final_seeds += [s for s in range(seeds[2 * i], seeds[2 * i] + seeds[2*i + 1])]
            print(final_seeds)
            continue
        if "map" in line:
            mapping = DefaultKeyDict()
            continue
        if not line and mapping is not None:
            mappings.append(mapping)
            mapping.sort()
            continue
        if not line:
            continue
        dest, src, l = line.split()
        dest = int(dest)
        src = int(src)
        l = int(l)
        mapping.set_many(dest, src, l)

    mappings.append(mapping)
    mapping.sort()
    # for m in mappings:
        # print(m)
    min_location = min(aam(mappings, final_seeds))
    print(min_location)