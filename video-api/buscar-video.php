<?php
// Endpoint de busca de vídeos/tutoriais da BSTEN (versão PHP).
// Coloque este arquivo e o videos.json na mesma pasta (ex.: /api/).
// Uso: GET /api/buscar-video.php?q=como funciona o bloqueio
header("Content-Type: application/json; charset=utf-8");

function normalizar($s) {
  $s = mb_strtolower($s, "UTF-8");
  $s = iconv("UTF-8", "ASCII//TRANSLIT//IGNORE", $s); // remove acentos
  $s = preg_replace("/[^a-z0-9\s]/", " ", $s);
  $s = preg_replace("/\s+/", " ", $s);
  return trim($s);
}

$q = "";
if (isset($_GET["q"])) {
  $q = $_GET["q"];
} else {
  $body = json_decode(file_get_contents("php://input"), true);
  if (is_array($body)) {
    $q = isset($body["q"]) ? $body["q"] : (isset($body["query"]["q"]) ? $body["query"]["q"] : "");
  }
}

$catalogo = json_decode(file_get_contents(__DIR__ . "/videos.json"), true);
$itens = isset($catalogo["itens"]) ? $catalogo["itens"] : [];

$consulta = normalizar($q);
$resultado = ["found" => false];

if ($consulta !== "") {
  $tokens = array_filter(explode(" ", $consulta), function ($t) { return strlen($t) >= 3; });
  $melhor = null; $melhorScore = 0;

  foreach ($itens as $item) {
    $score = 0;
    foreach (($item["keywords"] ?? []) as $kw) {
      $k = normalizar($kw);
      if ($k === "") continue;
      if (strpos($consulta, $k) !== false) $score += 3 + strlen($k) / 10;
      foreach ($tokens as $t) {
        if ($k === $t) $score += 2;
        elseif (strpos($k, $t) !== false || strpos($t, $k) !== false) $score += 1;
      }
    }
    if ($score > $melhorScore) { $melhorScore = $score; $melhor = $item; }
  }

  if ($melhor && $melhorScore >= 2) {
    if (empty($melhor["url"])) {
      $resultado = ["found" => false, "tema" => $melhor["tema"]];
    } else {
      $resultado = [
        "found" => true,
        "title" => $melhor["titulo"],
        "url"   => $melhor["url"],
        "theme" => $melhor["tema"],
        "type"  => $melhor["tipo"],
      ];
    }
  }
}

echo json_encode($resultado, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
