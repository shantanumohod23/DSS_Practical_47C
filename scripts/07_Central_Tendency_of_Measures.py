# Central Tendency of Measures

import statistics  

# Sample age data
age = [21, 21, 22, 23, 22, 21, 23, 21, 21, 21, 22, 23, 22, 21, 23, 21, 21, 21, 22, 23, 22]

# Calculating mean, median, and mode
mean_value = statistics.mean(age)  
median_value = statistics.median(age)  
mode_value = statistics.mode(age)  

# Display results
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
