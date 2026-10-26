<?php
namespace GCPRO\Atomic;

use Elementor\Modules\AtomicWidgets\Elements\Base\Atomic_Widget_Base;
use Elementor\Modules\AtomicWidgets\Elements\Base\Has_Template;
use Elementor\Modules\AtomicWidgets\Controls\Section;
use Elementor\Modules\AtomicWidgets\Controls\Types\Text_Control;
use Elementor\Modules\AtomicWidgets\Controls\Types\Select_Control;
use Elementor\Modules\AtomicWidgets\PropTypes\Classes_Prop_Type;
use Elementor\Modules\AtomicWidgets\PropTypes\Primitives\String_Prop_Type;

if ( ! defined( 'ABSPATH' ) ) { exit; }

class Trustindex_Badge extends Atomic_Widget_Base {
	use Has_Template;
	public static $widget_description = 'Editable Trustindex widget using the official loader.';
	protected $version = '0.4.2';
	public static function get_element_type(): string { return 'gcpro-trustindex'; }
	public function get_title() { return 'GCPRO Trustindex Reviews'; }
	public function get_icon() { return 'eicon-star'; }
	public function get_keywords() { return [ 'trustindex', 'reviews', 'rating', 'gcpro' ]; }
	public static function get_computed_html_tag( array $settings ): string { return 'div'; }
	protected static function define_props_schema(): array {
		return [
			'classes' => Classes_Prop_Type::make()->default( [] ),
			'widget_id' => String_Prop_Type::make()->default( '' ),
			'visibility' => String_Prop_Type::make()->enum( [ 'none', 'show' ] )->default( 'none' ),
		];
	}
	protected function define_atomic_controls(): array {
		return [ Section::make()->set_label( 'Trustindex Reviews' )->set_id( 'content' )->set_items( [
			Text_Control::bind_to( 'widget_id' )->set_label( 'Trustindex Widget ID' ),
			Select_Control::bind_to( 'visibility' )->set_label( 'Display reviews' )->set_options( [
				[ 'value' => 'none', 'label' => 'Hidden' ],
				[ 'value' => 'show', 'label' => 'Visible' ],
			] ),
		] ) ];
	}
	protected function get_templates(): array {
		return [ 'gcpro/atomic/trustindex' => __DIR__ . '/trustindex-badge.html.twig' ];
	}
}
