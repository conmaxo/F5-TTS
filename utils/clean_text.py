from vi_cleaner.vi_cleaner import ViCleaner
import re

def clean_text(text: str) -> str:
    """
    Clean the input text by removing special characters and extra spaces.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    pattern = r"[\u3000-\u303f\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\u2600-\u26ff\u25a0-\u25ff\u2700-\u27bf\U0001f600-\U0001f64f\U0001f300-\U0001f5ff\U0001f680-\U0001f6ff【】☉★☆♥♠♣♦←→↑↓∞≈≠±×÷€¥£₹₿αβγδπΣ∑∏_；]"

    text = (
        text.strip()
        .replace("  ", " ")
        .replace("”", "")
        .replace("“", "")
        .replace("—", "")
        .replace(":", ",")
        .replace("[", "")
        .replace("]", "")
        .replace("(", "")
        .replace(")", "")
        .replace("#", "")
        .replace("…", ". ")
        .replace("!", "\n")
        .replace("?", "\n")
        .replace("\n", ".")
        .replace("..", ". ")
        .replace("...", ", ")
    )

    text = re.sub(pattern, "", text)
    cleaner = ViCleaner(text)
    return cleaner.clean().strip()

if __name__ == "__main__":
    sample_text = "“Đầu Tư Thiên Mệnh Tộc Nhân, Thực Lực Của Ta Là Toàn Tộc Cộng Lại.\nVừa mở mắt, Khương Đạo Huyền đã ở trong thân xác tộc trưởng Khương gia. Đáng buồn thay, vì đột phá thất bại do đan dược bị hạ độc"
    cleaned_text = clean_text(sample_text)
    print("Original Text:", sample_text)
    print("Cleaned Text:", cleaned_text)