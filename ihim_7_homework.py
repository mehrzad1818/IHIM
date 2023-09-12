"""This is the 7th Python homework of IHIM Python Class."""
# %%

d1 = {1: "a", 2: "b", 3: "c", 4: "d"}
d2 = {2: "e", 4: "f", 5: "g"}


new_dict = {}

for d1_features in d1.values():
    for d2_features in d2.values():
        if d1_features[0] and d2_features[0] not in new_dict:
            new_dict = d1_features[0]
            new_dict = d2_features[0]


print(new_dict)
# %%
