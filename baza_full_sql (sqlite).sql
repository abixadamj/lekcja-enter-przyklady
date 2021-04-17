CREATE TABLE `Users` (
  `ID` int(11) NOT NULL,
  `Imie` text NOT NULL,
  `Nazwisko` text NOT NULL,
  `Password` text NOT NULL
) ;

--
-- Zrzut danych tabeli `Users`
--

INSERT INTO `Users` (`ID`, `Imie`, `Nazwisko`, `Password`) VALUES
(1, 'Adam', 'Jurkiewicz', 'fasdfasdfasdfasd'),
(2, 'Adam', 'Adamski', '5234523452345234'),
(3, 'Bartek', 'Kozłowski', 'dfafsdfasdfasdfdsaf'),
(4, 'Bartek', 'Kiszewski', '435234221223');

--
-- Indeksy dla zrzutów tabel
--


