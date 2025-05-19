import React from 'react';

function Navbar() {
  return (
    <nav className="bg-white shadow p-4 flex justify-between items-center">
      <h1 className="text-xl font-bold">Nusantara Flavours</h1>
      <div>
        <a href="#" className="mx-2">Home</a>
        <a href="#" className="mx-2">Resep</a>
        <a href="#" className="mx-2">Tentang</a>
      </div>
    </nav>
  );
}

export default Navbar;
