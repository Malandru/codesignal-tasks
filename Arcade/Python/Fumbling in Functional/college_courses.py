def collegeCourses(x, courses):
    def shouldConsider(course):
        return len(course) != x

    return list(filter(shouldConsider, courses))

x = 7
courses = ["Art", "Finance", "Business", "Speech", "History", "Writing", "Statistics"]

print(collegeCourses(x, courses))