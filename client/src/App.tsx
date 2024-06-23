import React, { useState, useRef, useEffect } from "react";
import ChessBoard from "./ChessBoard";
import BoardPermutationTable from "./BoardPermutationTable";
import LoadMore from "./LoadMore";
import "./App.css";

type Coordinate = {
  x: number;
  y: number;
};

const App: React.FC = () => {
  const [mainBoardCoordinates, setMainBoardCoordinates] = useState<
    Coordinate[]
  >([]);
  const [permutations, setPermutations] = useState<Coordinate[][]>([]);
  const [numPermutations, setNumPermutations] = useState<number>(0);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [page, setPage] = useState<number>(1);
  const scrollPosition = useRef<number>(0);

  const handleMainBoardChange = (coords: Coordinate[]) => {
    setMainBoardCoordinates(coords);
  };

  const handleCheckButtonClick = async () => {
    setErrorMessage(null);
    const permutations: Coordinate[][] = await fetchPermutationsFromBackend(
      mainBoardCoordinates,
      1,
    );
    setPermutations(permutations);
    setPage(2);
  };

  const handleClearButtonClick = () => {
    setMainBoardCoordinates([]);
    setPermutations([]);
    setNumPermutations(0);
    setErrorMessage(null);
    setPage(1);
  };

  const fetchPermutationsFromBackend = async (
    coords: Coordinate[],
    page: number,
  ): Promise<Coordinate[][]> => {
    const response = await fetch("http://127.0.0.1:5000/solve", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ rooks: serialize(coords), page, per_page: 10 }),
    });
    const rjson = await response.json();
    const data = rjson[0];
    if (data.error) {
      setErrorMessage(data.error);
      return [];
    }
    setNumPermutations(data.number_of_solutions);
    return data.solutions.map((solution: number[][]) => deserialize(solution));
  };

  const serialize = (coords: Coordinate[]): number[][] => {
    return coords.map((coord) => [coord.x, coord.y]);
  };

  const deserialize = (coords: number[][]): Coordinate[] => {
    return coords.map((coord) => ({ x: coord[0], y: coord[1] }));
  };

  const loadMorePermutations = async () => {
    if (page > Math.ceil(numPermutations / 10)) return;

    const newPermutations: Coordinate[][] = await fetchPermutationsFromBackend(
      mainBoardCoordinates,
      page,
    );
    setPermutations((prevPermutations) => [
      ...prevPermutations,
      ...newPermutations,
    ]);
    setPage((prevPage) => prevPage + 1);
  };

  return (
    <div className="App">
      <h1 className="text-center text-2xl mb-4">Justin's Rook Solver</h1>
      <div className="flex justify-center">
        <p className="text-center mb-4 w-2/3">
          Click on the chess board to place or remove rooks. Click "Check" to
          find all possible permutations.
        </p>
      </div>
      <div className="flex justify-center mb-8">
        <ChessBoard
          size={8}
          initialCoordinates={mainBoardCoordinates}
          onCoordinatesChange={handleMainBoardChange}
        />
      </div>
      <div className="flex justify-center mb-8">
        <button
          onClick={handleCheckButtonClick}
          className="bg-gradient-to-r from-blue-500 to-purple-500 hover:from-blue-700 hover:to-purple-700 text-white font-bold py-2 px-6 rounded-lg shadow-lg transform transition-transform duration-300 ease-in-out hover:scale-105 mr-4"
        >
          Check
        </button>
      </div>
      {errorMessage ? (
        <div className="flex justify-center mb-8">
          <p className="text-red-500">{errorMessage}</p>
        </div>
      ) : (
        <>
          <h1 className="text-center text-2xl mb-4">
            Possible Permutations ({numPermutations})
          </h1>
          <div className="flex justify-center">
            <BoardPermutationTable permutations={permutations} />
          </div>
          {page <= Math.ceil(numPermutations / 10) && (
            <LoadMore onLoadMore={loadMorePermutations} />
          )}
        </>
      )}
    </div>
  );
};

export default App;
