const predefinedQuestions = {
  food: "Allocate 15-25% of your budget for food, with flexibility for occasional splurges.",
  transportation: "Budget 10-20% for transportation, considering travel distances and chosen modes.",
  activities: "Allocate 15-20% for activities and attractions, adjusting based on the cost of your desired experiences.",
  "card-fees": "Knowing any transaction or foreign exchange fees helps you plan accordingly.",
  insurance: "Consider the cost and potential benefits of travel insurance."
};

const questionList = document.getElementById("question-list");
const aiMessage = document.querySelector(".ai-message p");

questionList.addEventListener("click", function(e) {
  if (e.target.classList.contains("question-button")) {
    const question = e.target.dataset.question;
    aiMessage.textContent = predefinedQuestions[question];
  }
});