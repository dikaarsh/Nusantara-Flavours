import React from 'react';
import Navbar from './components/Navbar';
import HeroSearch from './components/HeroSearch';
import RecipeList from './components/RecipeList';
import Footer from './components/Footer';

function App() {
  return (
    <div>
      <Navbar />
      <HeroSearch />
      <RecipeList />
      <Footer />
    </div>
  );
}

export default App;
