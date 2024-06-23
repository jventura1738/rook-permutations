import React, { useState } from "react";
import ChessBoard from "./ChessBoard";
import BoardPermutationTable from "./BoardPermutationTable";
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
  const [loading, setLoading] = useState<boolean>(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const handleMainBoardChange = (coords: Coordinate[]) => {
    setMainBoardCoordinates(coords);
  };

  const handleCheckButtonClick = async () => {
    setLoading(true);
    setErrorMessage(null);
    const permutations: Coordinate[][] =
      await fetchPermutationsFromBackend(mainBoardCoordinates);
    setPermutations(permutations);
    setLoading(false);
  };

  const serialize = (coords: Coordinate[]): number[][] => {
    return coords.map((coord) => [coord.x, coord.y]);
  };

  const deserialize = (coords: number[][]): Coordinate[] => {
    return coords.map((coord) => {
      return { x: coord[0], y: coord[1] };
    });
  };

  const fetchPermutationsFromBackend = async (
    coords: Coordinate[],
  ): Promise<Coordinate[][]> => {
    const response = await fetch("http://127.0.0.1:5000/solve", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ rooks: serialize(coords) }),
    });
    const data = await response.json();
    if (data[0].error) {
      setErrorMessage(data[0].error);
      return [deserialize([])];
    }
    const solutions = data[0].solutions;
    return solutions.map((solution: number[][]) => {
      return deserialize(solution);
    });
  };

  return (
    <div className="App">
      <h1 className="text-center text-2xl mb-4">Justin's Rook Solver</h1>
      <p className="text-center mb-4">
        Click on the chess board to place rooks. Click "Check" to find all
        possible permutations. An empty board will likely lag a lot.
      </p>
      <div className="flex justify-center mb-8">
        <ChessBoard
          size={8}
          initialCoordinates={mainBoardCoordinates}
          onCoordinatesChange={handleMainBoardChange}
        />
      </div>
      {loading ? (
        <>
          <div className="flex justify-center mb-8">
            <div className="w-10 h-10 border-4 border-blue-500 border-solid border-t-transparent rounded-full animate-spin"></div>
          </div>
          <p>
            Fun fact: an empty board must find 40320 chess boards! Please be
            patient...
          </p>
        </>
      ) : errorMessage ? (
        <div className="flex justify-center mb-8">
          <p className="text-red-500">{errorMessage}</p>
        </div>
      ) : (
        <>
          <div className="flex justify-center mb-8">
            <button
              onClick={handleCheckButtonClick}
              className="bg-gradient-to-r from-blue-500 to-purple-500 hover:from-blue-700 hover:to-purple-700 text-white font-bold py-2 px-6 rounded-lg shadow-lg transform transition-transform duration-300 ease-in-out hover:scale-105"
            >
              Check
            </button>
          </div>
          <h1 className="text-center text-2xl mb-4">
            Possible Permutations ({permutations.length})
          </h1>
          <div className="flex justify-center">
            <BoardPermutationTable permutations={permutations} />
          </div>
        </>
      )}
    </div>
  );
};

export default App;
