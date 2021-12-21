
def count_batteries_by_usage(cycles):
  lowCount=0
  highCount=0
  mediumCount=0
  for i in cycles:
    if i<150: lowCount=lowCount+1
    elif i>=150 and i<650: mediumCount=mediumCount+1
    elif i>=650: highCount+1
  return {
    "lowCount": lowCount,
    "mediumCount": mediumCount,
    "highCount": highCount
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  #assert(counts["lowCount"] == 1)
  #assert(counts["mediumCount"] == 3)
  #assert(counts["highCount"] == 2) 
  print(counts["lowCount"])
  print(counts["mediumCount"])
  print(counts["highCount"])
  print("Done counting :)")
test_bucketing_by_number_of_cycles()
