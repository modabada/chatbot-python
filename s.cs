void GenerateKingMoves () {
	for (int i = 0; i < kingMoves[friendlyKingSquare].Length; i++) {
		int targetSquare = kingMoves[friendlyKingSquare][i];
		int pieceOnTargetSquare = board.Square[targetSquare];

		// Skip squares occupied by friendly pieces
		if (Piece.IsColour (pieceOnTargetSquare, friendlyColour)) {
			continue;
		}

		bool isCapture = Piece.IsColour (pieceOnTargetSquare, opponentColour);
		if (!isCapture) {
			// King can't move to square marked as under enemy control, unless he is capturing that piece
			// Also skip if not generating quiet moves
			if (!genQuiets || SquareIsInCheckRay (targetSquare)) {
				continue;
			}
		}

		// Safe for king to move to this square
		if (!SquareIsAttacked (targetSquare)) {
			moves.Add (new Move (friendlyKingSquare, targetSquare));

			// Castling:
			if (!inCheck && !isCapture) {
				// Castle kingside
				if ((targetSquare == f1 || targetSquare == f8) && HasKingsideCastleRight) {
					int castleKingsideSquare = targetSquare + 1;
					if (board.Square[castleKingsideSquare] == Piece.None) {
						if (!SquareIsAttacked (castleKingsideSquare)) {
							moves.Add (new Move (friendlyKingSquare, castleKingsideSquare, Move.Flag.Castling));
						}
					}
				}
				// Castle queenside
				else if ((targetSquare == d1 || targetSquare == d8) && HasQueensideCastleRight) {
					int castleQueensideSquare = targetSquare - 1;
					if (board.Square[castleQueensideSquare] == Piece.None && board.Square[castleQueensideSquare - 1] == Piece.None) {
						if (!SquareIsAttacked (castleQueensideSquare)) {
							moves.Add (new Move (friendlyKingSquare, castleQueensideSquare, Move.Flag.Castling));
						}
					}
				}
			}
		}
	}
}