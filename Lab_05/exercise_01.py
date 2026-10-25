
# Campus Resource Tracker

resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]

def display_resources(resources):
    if len(resources) == 0:
        print("No resources found.")
        return

    for r in resources:
        if r[3] < 0:
            print("Invalid quantity for", r[1])
        else:
            print(r)

def search_by_category(resources, category):
    found = False

    for r in resources:
        if r[2] == category:
            print(r)
            found = True

    if found == False:
        print("Category not found.")

def find_unavailable(resources):
    found = False

    for r in resources:
        if r[3] == 0:
            print(r)
            found = True

    if found == False:
        print("No unavailable resources.")

print("All Resources:")
display_resources(resources)

print("\nElectronics:")
search_by_category(resources, "Electronics")

print("\nUnavailable Resources:")
find_unavailable(resources)

print("\nUnknown ID Test:")
search_by_id = 999
print("Unknown resource ID:", search_by_id)

print("\nNegative Quantity Test:")
display_resources([[106, "Printer", "Electronics", -2]])

print("\nEmpty List Test:")
display_resources([])
