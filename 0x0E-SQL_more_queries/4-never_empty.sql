-- creates new table with default value 1 for id
CREATE USER IF NOT EXISTS `id_not_null` (
    `id` INT DEFAULT 1,
    `name` VARCHAR(256)
)