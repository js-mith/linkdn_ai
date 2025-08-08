import random

def generate_post(name, industry, role, trends):
    # Simulate AI post generation (replace with OpenAI API if you have key)
    trend = random.choice(trends) if trends else "latest updates in your field"
    post = (
        f"As a {role} in the {industry} sector, I believe staying updated is key. "
        f"Today, I came across an interesting trend: '{trend}'. "
        f"It’s fascinating to see how our industry is evolving, and I’m excited to "
        f"leverage these changes for better results.\n\n"
        f"#Innovation #{industry.replace(' ', '')} #Growth"
    )
    return post
