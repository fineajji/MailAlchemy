# 📧 MailAlchemy

**MailAlchemy** is a Python-based tool designed to generate all possible email permutations from a given set of names. It supports original, lowercase, and uppercase email variations and is ideal for email enumeration, testing, and pattern discovery.

## ✨ Features

- Generate multiple email permutations from a list of names.
- Supports original, lowercase, and uppercase permutations.
- Customizable domain for easy integration.
- CLI-based tool for simple usage.

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:fineajji/MailAlchemy.git
    cd MailAlchemy
    ```

2. Ensure you have Python 3 installed:

    ```bash
    python3 --version
    ```

### Usage

Once the script is downloaded, you can use **MailAlchemy** to generate email permutations from a text file of names.

```bash
python3 MailAlchemy.py -d <domain> -f <input_file> -o <output_file>
```

- `-d <domain>`: The email domain (e.g., `example.com`).
- `-f <input_file>`: File containing names (one per line).
- `-o <output_file>`: File to write the generated email permutations.

#### Example

```bash
python3 MailAlchemy.py -d example.com -f names.txt -o output.txt
```

### Output Example

For the name "David Anderson" and domain `example.com`, **MailAlchemy** will generate permutations like:

```bash
David.Anderson@example.com
david.anderson@example.com
DAVID.ANDERSON@example.com
D.Anderson@example.com
...
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🧙‍♂️ Author

- **[fineajji](https://github.com/fineajji)** - Creator of MailAlchemy

---

Made with ❤️ using Python.
