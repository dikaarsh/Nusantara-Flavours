import React from 'react';
import RecipeCard from './RecipeCard';

function RecipeList() {
  const dummyData = [
    { id: 1, title: 'Rawon', description: 'Daging sapi dengan kuah kluwek.' },
    { id: 2, title: 'Soto Lamongan', description: 'Soto khas Lamongan dengan koya.' },
  ];

  return (
    <div className="p-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {dummyData.map((recipe) => (
        <RecipeCard key={recipe.id} title={recipe.title} description={recipe.description} />
      ))}
    </div>
  );
}

export default RecipeList;
