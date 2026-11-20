from flask import Flask, render_template, request

app = Flask(
     __name__,
     template_folder="app/templates",
     static_folder="app/static"
)
OPPORTUNITIES = [
    {
        "name": "Digital Marketing Services",
        "category": "Technology",
        "skills": ["technology", "marketing", "design", "communication"],
        "interests": ["technology", "digital services", "marketing"],
        "min_budget": 50000,
        "description": "Help local businesses grow through social media, branding and online marketing."
    },
    {
        "name": "Poultry Farming",
        "category": "Agriculture",
        "skills": ["agriculture", "business", "management"],
        "interests": ["agriculture", "food", "farming"],
        "min_budget": 150000,
        "description": "Start a small poultry project supplying eggs or chickens to local markets."
    },
    {
        "name": "Graphic Design Studio",
        "category": "creative",
        "skills": ["design", "technology", "digital services"],
        "interests": ["technology", "digital services", "design"],
        "min_budget": 30000,
        "description": "Offer logos, posters and visual branding services to individuals and businesses."
    },
    {
        "name": "Clothing and Fashion",
        "category": "Fashion",
        "skills": ["design", "creativity", "sales"],
        "interests": ["fashion", "design", "retail"],
        "min_budget": 100000,
        "description": "Start a small clothing, tailoring or fashion retail business."
    },
    {
        "name": "Tutoring services",
        "category": "Education",
        "skills": ["teaching", "communication", "technology"],
        "interests": ["education", "technology", "community services"],
        "min_budget": 20000,
        "description": "Provide tutoring, academic support or digital learning services."
    }
]
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/explore", methods=["GET", "POST"])
def explore():
    if request.method == "POST":
        location = request.form.get("location", "").strip()
        skills = request.form.get("skills", "").lower()
        interests = request.form.get("interests", "").lower()
        try:
            budget = float(request.form.get("budget", 0))
        except ValueError:
            budget = 0
        results = [] 
        for opportunity in OPPORTUNITIES:
            matching_skills = [
                skill for skill in opportunity.get("skills", [])
                if skill in skills
            ]
            skills_score = (
                len(matching_skills) /
                max(len(opportunity.get("skills", [])), 1)
            ) * 35
            matching_interests = [
                interest for interest in opportunity.get("interests", [])
                if interest in interests
            ]
            interests_score = (
                len(matching_interests) /
                max(len(opportunity.get("interests", [])), 1)
            ) * 25
            minimum_budget = opportunity["min_budget"]
            if budget >= minimum_budget:
                finance_score = 25
            else:
                finance_score = (
                    budget / minimum_budget
                ) * 25 if minimum_budget > 0 else 0
            environment_score = 0
            total_score = (
                    skills_score
                    + interests_score
                    + finance_score
                    + environment_score
                )
            if total_score > 0:
                results.append({
                    **opportunity,
                    "score": round(total_score),
                    "skills_score": round(skills_score),
                    "interests_score": round(interests_score),
                    "finance_score": round(finance_score),
                    "environment_score": round(environment_score),
                    "matching_skills": matching_skills,
                    "matching_interests": matching_interests
                })        
        results.sort(key=lambda item: item["score"], reverse=True)
        return render_template(
            "explore.html",
            results=results,
            location=location,
            budget=budget,
            searched=True
        )           
    return render_template(
        "explore.html",
        results=[],
        location="",
        budget="",
        searched=False
    )                    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)