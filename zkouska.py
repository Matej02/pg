def process_strings(strings):
    result = []
    
    for s in strings:
        if s == "STOP":
            break
        if len(s) > 3:
            result.append(s.upper())
    
    return result

if __name__ == "__main__":
    test_cases = [
        ["abc", "abcd", "STOP", "efgh"],
        ["hello", "world", "STOP", "python"],
        ["hi", "ok", "go"],
        ["code", "test", "debug"]
    ]
    
    for i, test_case in enumerate(test_cases, start=1):
        print(f"Test {i}: {test_case}")
        result = process_strings(test_case)
        print("Výsledek:", result)
        
