const snakeToCamel = (s) => {
  return s.replace(/([_][a-z])/gi, ($1) => {
    return $1.toUpperCase().replace("_", "");
  });
};
