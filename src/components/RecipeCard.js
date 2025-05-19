import React from 'react';

function RecipeCard({ title, description }) {
  return (
    <div className="border rounded shadow p-4">
      <h3 className="text-xl font-semibold mb-2">{title}</h3>
      <p>{description}</p>
    </div>
  );
}

export default RecipeCard;
