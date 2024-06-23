import React, { useState, useEffect } from "react";

export type Coordinate = {
  x: number;
  y: number;
};

type ChessBoardProps = {
  size: number;
  readonly?: boolean;
  cellSize?: number;
  initialCoordinates?: Coordinate[];
  onCoordinatesChange?: (coords: Coordinate[]) => void;
};

const ChessBoard: React.FC<ChessBoardProps> = ({
  size,
  readonly = false,
  cellSize = 50,
  initialCoordinates = [],
  onCoordinatesChange,
}) => {
  const [activeCells, setActiveCells] =
    useState<Coordinate[]>(initialCoordinates);

  useEffect(() => {
    setActiveCells(initialCoordinates);
  }, [initialCoordinates]);

  useEffect(() => {
    if (onCoordinatesChange) {
      onCoordinatesChange(activeCells);
    }
  }, [activeCells, onCoordinatesChange]);

  const toggleCell = (x: number, y: number) => {
    if (readonly) return;
    const index = activeCells.findIndex((cell) => cell.x === x && cell.y === y);
    if (index === -1) {
      setActiveCells([...activeCells, { x, y }]);
    } else {
      setActiveCells(
        activeCells.filter((cell) => !(cell.x === x && cell.y === y)),
      );
    }
  };

  const isCellActive = (x: number, y: number) => {
    return activeCells.some((cell) => cell.x === x && cell.y === y);
  };

  return (
    <div
      className="grid outline"
      style={{
        gridTemplateColumns: `repeat(${size}, ${cellSize}px)`,
        gridTemplateRows: `repeat(${size}, ${cellSize}px)`,
      }}
    >
      {Array.from({ length: size }, (_, rowIndex) =>
        Array.from({ length: size }, (_, colIndex) => (
          <div
            key={`${rowIndex}-${colIndex}`}
            onClick={() => toggleCell(colIndex, rowIndex)}
            className={`border border-black flex items-center justify-center ${readonly ? "cursor-default" : "cursor-pointer"}`}
            style={{
              width: `${cellSize}px`,
              height: `${cellSize}px`,
              backgroundColor:
                (rowIndex + colIndex) % 2 === 0 ? "white" : "lightgray",
              fontSize: `${cellSize * 0.6}px`,
              lineHeight: `${cellSize}px`,
            }}
          >
            {isCellActive(colIndex, rowIndex) ? "♜" : ""}
          </div>
        )),
      )}
    </div>
  );
};

export default ChessBoard;
