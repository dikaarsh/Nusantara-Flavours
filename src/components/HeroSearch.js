import React from 'react';

function HeroSearch() {
  return (
    <div className="bg-gray-100 p-10 text-center">
      <h2 className="text-3xl mb-4">Cari Resep Masakan Nusantara</h2>
      <input className="border p-2 w-1/2" type="text" placeholder="Cari resep..." />
    </div>
  );
}

export default HeroSearch;
