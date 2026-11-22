function explore(){
    alert(
        "Welcome to IMBUTO!\n\n" +
        "Your journey to discovering business opportunities starts here."
    );
}
document.addEventListener("DOMContentLoaded", function (){
    const searchInput = document.getElementById("searchInput");
    const categoryFilter = document.getElementById("categoryFilter");
    const sortFilter = document.getElementById("sortFilter");
    const featureGrid = document.querySelector(".feature-grid");
    if(!searchInput || !categoryFilter || !sortFilter || !featureGrid){
        return;
    }
    const cards = Array.from(featureGrid.querySelectorAll(".feature"));
    function filterAndSortOpportunities(){
        const searchText = searchInput.value.toLowerCase().trim();
        const selectedCategory = categoryFilter.value.toLowerCase();
        const sortOrder = sortFilter.value;
        const visibleCards = cards.filter(card =>{
            const name = card.querySelector("h3").textContent.toLowerCase();
            const category = card.querySelector(".tag").textContent.toLowerCase();
            const matchesSearch = name.includes(searchText);
            const matchesCategory = !selectedCategory || category === selectedCategory;
            card.style.display = matchesSearch && matchesCategory ? "" : "none";
            return matchesSearch && matchesCategory;
        });
        visibleCards.sort((a,b) =>{
            const scoreA = Number(a.dataset.score);
            const scoreB = Number(b.dataset.score);
            return sortOrder === "high"
                ? scoreB - scoreA
                : scoreA - scoreB;
        });
        visibleCards.forEach(card => featureGrid.appendChild(card));
    }
    searchInput.addEventListener("input", filterAndSortOpportunities);
    categoryFilter.addEventListener("change", filterAndSortOpportunities);
    sortFilter.addEventListener("change", filterAndSortOpportunities);
});