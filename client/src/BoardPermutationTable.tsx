import React from "react";
import ChessBoard, { Coordinate } from "ChessBoard";

type BoardPermutationTableProps = {
  permutations: Coordinate[][];
};

const BoardPermutationTable: React.FC<BoardPermutationTableProps> = ({
  permutations,
}) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
      {permutations.map((coords, index) => (
        <ChessBoard
          key={index}
          size={8}
          readonly={true}
          cellSize={30}
          initialCoordinates={coords}
        />
      ))}
    </div>
  );
};

export default BoardPermutationTable;
