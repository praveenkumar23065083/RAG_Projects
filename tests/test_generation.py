from src.generation.generator import generate_answer


query = "What is DeepOKAN?"


retrieved_chunks = [
    {
        "id": "test_1",
        "text": (
            "DeepOKAN is a Deep Operator Network based on "
            "Kolmogorov Arnold Networks for solving mechanics problems."
        ),
        "document_name": "DeepOKAN2.pdf",
        "page_number": 1
    },
    {
        "id": "test_2",
        "text": (
            "The DeepOKAN architecture replaces the conventional "
            "MLP-based branch network with a KAN-based architecture."
        ),
        "document_name": "DeepOKAN2.pdf",
        "page_number": 3
    }
]


answer = generate_answer(
    query,
    retrieved_chunks
)


print("\nAnswer:\n")

print(answer)